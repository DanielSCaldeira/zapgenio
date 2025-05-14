import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("API_KEY_OPENAI"),
)



# Prompt da tarefa
def ia_prompt_limpesa_conteudo(texto_bruto):
    prompt = f"""
        Você é um assistente especializado em organização e estruturação de textos brutos, como os extraídos de sites, catálogos, e-commerces ou documentos técnicos.
        Ao receber um texto com informações repetidas, bagunçadas ou soltas, sua tarefa é:
        - Eliminar repetições, palavras isoladas e ruídos que não agregam informação útil.
        - Preservar todos os dados relevantes
        - Preservar todos os dados relevantes, como nomes de produtos, marcas, categorias, especificações técnicas, capacidades ou descrições. 
        - Organizar as informações em formato de lista estruturada, separada por seções temáticas como "Produtos", "Marcas", "Calibres", "Capacidades", etc.
        - Não criar textos institucionais ou promocionais. Apenas limpe e organize o conteúdo técnico.
        Texto bruto:
        \"\"\"{texto_bruto}\"\"\"
        Retorne apenas o texto final limpo, estruturado e resumido, **sem usar formatação especial como asteriscos, negrito, itálico, markdown ou HTML**. Apenas texto puro com listas simples.
        """
    
    return prompt


def ia_texto_bruto(texto_bruto):
    prompt = ia_prompt_limpesa_conteudo(texto_bruto)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # ou gpt-4 se preferir
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em limpeza e reescrita de textos brutos."},
            {"role": "user", "content": prompt.strip()}
        ],
        max_tokens=800,  # Limite para o número de tokens gerados na resposta
        temperature=0.7
    )

    # Resultado final
    texto_limpo = response.choices[0].message.content # Corrigido para 'text'
    print(texto_limpo)
