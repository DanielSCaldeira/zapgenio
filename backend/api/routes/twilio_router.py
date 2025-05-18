from fastapi import APIRouter, Request, Form
from twilio.rest import Client
import os
from dotenv import load_dotenv
from fastapi.responses import PlainTextResponse

load_dotenv()

router = APIRouter()

# Twilio config
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")

# Valida as variáveis
if not all([account_sid, auth_token, from_whatsapp]):
    raise ValueError("Algumas variáveis de ambiente do Twilio não estão definidas.")

client = Client(account_sid, auth_token)

@router.get("/")
async def check_whatsapp():
    return {"status": "Webhook Twilio GET ativo"}

@router.post("/", response_class=PlainTextResponse)
async def handle_whatsapp_message(request: Request):
    form = await request.form()
    from_number = form.get("From")
    body = form.get("Body")

    if not from_number or not body:
        return PlainTextResponse("Dados inválidos recebidos", status_code=400)

    print(f"Mensagem recebida de {from_number}: {body}")

    try:
        client.messages.create(
            from_=from_whatsapp,
            to=from_number,
            body="Olá! Recebemos sua mensagem no ZapGênio. ✅"
        )
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        return PlainTextResponse("Erro interno ao processar", status_code=500)

    return "Mensagem processada"
