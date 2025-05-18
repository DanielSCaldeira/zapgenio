from fastapi import APIRouter, Depends, HTTPException, Request, requests
import os
from dotenv import load_dotenv
import httpx

load_dotenv()

router = APIRouter()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
# Defina os dados necessários
PHONE_NUMBER_ID = "102839283923823"
# Rota para listar todos os compromissos (GET)
@router.get("/")
async def verify(request: Request):
    args = request.query_params
    mode = args.get("hub.mode")
    token = args.get("hub.verify_token")
    challenge = args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return int(challenge)
        else:
            return {"error": "Token inválido"}
    return {"error": "Requisição inválida"}

# Rota para receber mensagens do WhatsApp
@router.post("/")
async def receive_whatsapp_message(request: Request):
    body = await request.json()
    print("📩 Mensagem recebida:", body)
    return {"status": "received"}

@router.get("/enviar_mensagem")
async def send_message(destinatario: str, mensagem: str):
    # Montando o payload para o WhatsApp API
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Aqui, o "destinatario" será o número para quem a mensagem será enviada
    data = {
        "messaging_product": "whatsapp",
        "to": destinatario,  # Número do destinatário
        "type": "text",
        "text": {
            "body": mensagem  # Conteúdo da mensagem
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

    # Verificando se a resposta foi bem-sucedida
    if response.status_code == 200:
        return {"status": "success", "message": "Mensagem enviada com sucesso!"}
    else:
        raise HTTPException(status_code=response.status_code,  detail={
            "message": "Erro ao enviar mensagem",
            "whatsapp_response": response.text
        })
