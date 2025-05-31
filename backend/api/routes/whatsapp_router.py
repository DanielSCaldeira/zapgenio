from fastapi import APIRouter, HTTPException, Request, Query
import os
from dotenv import load_dotenv
import httpx
import logging
import re


# Configuração do logger
logger = logging.getLogger("uvicorn")

load_dotenv()

router = APIRouter()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")
PHONE_NUMBER_ID = "711792312006625"

# ✅ Função para enviar mensagem interativa com botões
async def enviar_mensagem_com_botoes(destinatario: str, nome: str):
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messaging_product": "whatsapp",
        "to": normalizar_numero_brasil(destinatario),
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": f"Olá, {nome}! O que gostaria de fazer?"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "marcar_agenda",
                            "title": "Marcar Agenda"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "tirar_duvidas",
                            "title": "Tirar Dúvidas"
                        }
                    }
                ]
            }
        }
    }
    try:
        async with httpx.AsyncClient(timeout=50.0) as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()  # Força exceção para status HTTP 4xx/5xx

        logger.info("✅ Mensagem enviada com sucesso.")

    except httpx.HTTPStatusError as http_err:
        logger.error(f"❌ Erro HTTP ao enviar mensagem: {http_err.response.status_code} - {http_err.response.text}")
    except httpx.ConnectTimeout as timeout_err:
        logger.error(f"❌ Conexão expirou: {timeout_err}", exc_info=True)
    except httpx.RequestError as req_err:
        logger.error(f"❌ Erro de requisição: {req_err.__class__.__name__} - {req_err}", exc_info=True)
    except Exception as e:
        logger.error(f"❌ Erro inesperado ao processar mensagem: {e}")
   



# ✅ Rota de verificação do Webhook
@router.get("/")
async def verify(request: Request):
    args = request.query_params
    mode = args.get("hub.mode")
    token = args.get("hub.verify_token")
    challenge = args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == WHATSAPP_VERIFY_TOKEN:
            return int(challenge)
        else:
            raise HTTPException(status_code=403, detail="Token inválido")
    raise HTTPException(status_code=400, detail="Requisição inválida")

# ✅ Rota para receber mensagens do WhatsApp
@router.post("/")
async def receive_whatsapp_message(request: Request):
    body = await request.json()
    logger.info(f"📩 Mensagem recebida: {body}")

    try:
        entry = body['entry'][0]
        change = entry['changes'][0]
        value = change['value']

        nome_remetente = value['contacts'][0]['profile']['name']
        wa_id = value['contacts'][0]['wa_id']
        mensagem = value['messages'][0]['text']['body']
        mensagem_id = value['messages'][0]['id']
        timestamp = value['messages'][0]['timestamp']

        dados_importantes = {
            "nome_remetente": nome_remetente,
            "wa_id": wa_id,
            "mensagem": mensagem,
            "mensagem_id": mensagem_id,
            "timestamp": timestamp
        }

        logger.info(f"✅ Dados extraídos: {dados_importantes}")

        # ✅ Envia mensagem com botões
        await enviar_mensagem_com_botoes(wa_id, nome_remetente)

    except Exception as e:
        logger.error(f"❌ Erro ao processar mensagem: {e}")

    return {"status": "received"}

# ✅ Rota para enviar mensagens simples
@router.get("/enviar_mensagem")
async def send_message(
    destinatario: str = Query(..., description="Número do destinatário no formato E.164"),
    mensagem: str = Query(..., description="Texto da mensagem")
):
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": destinatario,
        "type": "text",
        "text": {"body": mensagem}
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return {"status": "success", "message": "Mensagem enviada com sucesso!"}
    else:
        raise HTTPException(status_code=response.status_code, detail={
            "message": "Erro ao enviar mensagem",
            "whatsapp_response": response.text
        })


def normalizar_numero_brasil(numero: str) -> str:
    """
    Normaliza números brasileiros adicionando o '9' no início do número
    se for de celular e estiver faltando.

    Parâmetro:
        numero (str): Número no formato E.164 (ex: '+5561995948398') ou nacional (ex: '061995948398')

    Retorna:
        str: Número normalizado no formato E.164.
    """
    # Remove qualquer caractere não numérico
    numero_limpo = re.sub(r'\D', '', numero)

    # Verifica se já tem o código do país
    if numero_limpo.startswith('55'):
        numero_nacional = numero_limpo[2:]
    else:
        numero_nacional = numero_limpo

    # Extrai DDD e número
    ddd = numero_nacional[:2]
    numero_principal = numero_nacional[2:]

    # Se já tiver 9 dígitos, assume que está correto
    if len(numero_principal) == 9:
        pass
    # Se tiver 8 dígitos, pode ser celular sem o 9 ou telefone fixo
    elif len(numero_principal) == 8:
        # Se o primeiro dígito for de 6 a 9, é fixo; se for 9, já está certo
        primeiro_digito = numero_principal[0]
        if primeiro_digito in ['6', '7', '8']:
            # Telefone fixo, não adiciona nada
            pass
        else:
            # Adiciona '9' no início, padrão para celular
            numero_principal = '9' + numero_principal
    else:
        # Caso atípico: número muito longo ou muito curto
        raise ValueError(f"Número inválido: {numero}")

    # Retorna no formato E.164
    return f"+55{ddd}{numero_principal}"
