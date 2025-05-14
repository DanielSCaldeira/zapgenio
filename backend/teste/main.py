import sys
import os
import asyncio
from backend.services.pergunta_resposta_service import PerguntaRespostaService
from backend.utils.prompt_limpesa_conteudo import ia_texto_bruto

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from urllib.parse import urljoin, urlparse
from backend.models import initialize_sql  # Ajuste aqui
from backend.database.connection import AsyncSessionLocal
from backend.models.pergunta_resposta import PerguntaResposta
from backend.services.vetor_service import VetorService
import difflib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import hashlib
import unicodedata
import re
from newspaper import Article
import time
from readability import Document


async def main():
    # await process_pergunta_resposta()
    crawl_site("https://www.casadotiro.com.br/")
    
def get_all_links(url):
    """Obtém todos os links internos de uma página."""
    links = set()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.strip():
                absolute_url = urljoin(urlparse(url).netloc, href)
                if urlparse(absolute_url).netloc == urlparse(url).netloc and absolute_url not in links:
                    links.add(absolute_url)
    except Exception as e:
        print(f"[ERRO] Falha ao obter links de {url}: {e}")
    return links

def extract_content_from_article(url):
    """Extrai título e texto principal usando newspaper3k."""
    article = Article(url)
    article.download()
    article.parse()
    return article.title, article.text

def crawl_site(start_url):
    """Percorre o site, extrai dados e salva em lista de resultados."""
    visited = set()
    to_visit = {start_url}
    resultados = []
    urlPrincipal = urlparse(start_url).netloc
    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue

        print(f"Visitando: {url}")
        visited.add(url)

        try:
            # titulo, conteudo = extract_content_from_article(url)
            titulo, conteudo = extract_content_from_article2(url)
            if conteudo.strip():
                resultados.append({
                    'url': url,
                    'titulo': titulo,
                    'texto': conteudo
                })
                print(f"[SUCESSO] Conteúdo extraído de: {url}")
            else:
                print(f"[AVISO] Nenhum conteúdo encontrado em: {url}")
        except:
            print(f"[ERRO] Falha ao extrair de {url}")

        novos_links = get_all_links(url)
        to_visit.update(set(novos_links) - visited)
        print(f"Quantidade de links {len(to_visit)} -> Quantidade de visitados {len(visited)}")
        time.sleep(1)  # evita sobrecarregar o servidor
    textos_limpos = limpar_textos(resultados)
    return textos_limpos

from readability import Document
import requests
from bs4 import BeautifulSoup

def extract_content_from_article2(url):
    """Extrai TODO o texto visível da página HTML."""
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    doc = Document(response.text)
    # Extrair título
    titulo = doc.title()
    
    # Remove scripts, styles e outros elementos não visíveis
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()

    # Extrai todo o texto visível
    texto = soup.get_text(separator='\n', strip=True)
    return titulo, texto


def extrair_conteudo(url_base: str, profundidade=1) -> list[dict]:
    """Extrai conteúdo textual do site e organiza por seções, limitado ao domínio base e sem duplicatas."""
    visitados = set()
    fila = [(url_base, 0)]  # Armazena tupla (url, nivel)
    resultados = []
    hashes_conteudo = set()

    dominio_base = urlparse(url_base).netloc

    while fila:
        url, nivel = fila.pop(0)
        if url in visitados or nivel > profundidade:
            continue
        visitados.add(url)

        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code != 200:
                continue
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")
            continue

        soup = BeautifulSoup(resp.text, 'html.parser')

        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'noscript', 'form']):
            tag.decompose()

        titulo = soup.title.string.strip() if soup.title and soup.title.string else url

        textos = [
            t for t in (
                p.get_text(separator=' ', strip=True)
                for p in soup.find_all(['p', 'li'])
            )
            if t.strip()
        ]
        conteudo = "\n".join(textos)

        hash_conteudo = hashlib.sha256(conteudo.encode('utf-8')).hexdigest()
        if hash_conteudo in hashes_conteudo or not conteudo:
            continue
        hashes_conteudo.add(hash_conteudo)

        resultados.append({
            'url': url,
            'titulo': titulo,
            'texto': conteudo
        })

        # Adiciona novos links internos com o próximo nível
        for a in soup.find_all('a', href=True):
            novo_link = urljoin(url, a['href'])
            dominio_novo = urlparse(novo_link).netloc
            if dominio_novo == dominio_base and novo_link not in visitados:
                fila.append((novo_link, nivel + 1))
                if len(fila) == 15:
                    break
    
    textosLimpos  = limpar_textos(resultados)
    return textosLimpos

def normalize(texto: str) -> str:
    """
    Pré-limpa e normaliza o texto bruto, removendo ruídos visuais e técnicos,
    preservando informações úteis como datas, números e promoções.
    Retorna o texto em letras minúsculas.
    """
    if not texto or texto.strip() == "":
        return ""

    texto = texto.lower()

    # Remove acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    # Remove tags HTML
    texto = re.sub(r"<[^>]+>", " ", texto)

    # Remove URLs
    texto = re.sub(r"http\S+|www\.\S+", " ", texto)

    # Remove emojis e caracteres não ASCII visíveis
    texto = re.sub(r"[^\x00-\x7F]+", " ", texto)

    # Substitui múltiplos símbolos repetidos (!!!, ???, ---) por um só
    texto = re.sub(r"([!?.,\-])\1+", r"\1", texto)

    # Remove caracteres especiais, preservando números, %, /, ()
    texto = re.sub(r"[^\w\s.,;:!?%/()\-]", " ", texto)

    # Reduz espaços múltiplos
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()

def get_similar_substring(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    matcher = difflib.SequenceMatcher(a=words1, b=words2)
    for block in matcher.get_matching_blocks():
        if block.size == 0:
            continue
        yield ' '.join(words1[block.a: block.a + block.size])

def similar_text(text_list, key="texto"):
    textoIgual = []
   
    for i in range(len(text_list) - 1):  # evita ultrapassar o tamanho da lista
        text1 = normalize(text_list[i][key])
        text2 = normalize(text_list[i + 1][key])
        lista = get_similar_substring(text1, text2)
        for trecho in lista:
            if trecho and trecho not in textoIgual and len(trecho) > 50:
                textoIgual.append(trecho)

    return textoIgual

def limpar_textos(text_list, key="texto"):
    similares = similar_text(text_list, key)
    textos_limpos = []

    for item in text_list:
        texto = normalize(item[key])
        print(f"Texto original: {len(texto)}")
        for trecho in similares:
            if trecho in texto:
                texto = texto.replace(trecho, "")
        
        if texto.isspace() or not texto:
            continue    
        print(f"Texto regatorado: {len(texto)}") 
        texto = ia_texto_bruto(texto.strip()) 
        pergunta = ia_texto_bruto(texto.strip()) 
        textos_limpos.append({
            item['url']: item['url'],
            item['titulo']: item['titulo'],
            key: texto
            item['Pergunta': item['Pergunta'],:
            })

    return textos_limpos

async def process_pergunta_resposta():
    async with AsyncSessionLocal() as db:
        lista: list[PerguntaResposta] = await PerguntaRespostaService(db).list()

        for pergunta_resposta in lista:
            if pergunta_resposta:
                vetorService = VetorService(db)
                vetor = await vetorService.gerar_embedding_pergunta(pergunta_resposta.pergunta)
                await vetorService.salvar_vetor_na_base(pergunta_resposta.id, vetor)
            else:
                print(f"PerguntaResposta com ID {id} não encontrada.")
        vetorService = VetorService(db)
        g = await vetorService.buscar_similares("Qual é o horário de funcionamento?")
        print(g)

# Roda a função principal
if __name__ == "__main__":
    asyncio.run(main())
