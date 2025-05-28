import os
from twilio.rest import Client
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

class TwilioService:
    def __init__(self):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
        to_whatsapp = os.getenv("TWILIO_WHATSAPP_TO")

        if not all([account_sid, auth_token, from_whatsapp, to_whatsapp]):
            raise ValueError("Variáveis de ambiente Twilio não configuradas corretamente")

        self.client = Client(account_sid, auth_token)
        self.from_whatsapp = from_whatsapp
        self.to_whatsapp = to_whatsapp

    def enviar_mensagem(self, to_number: str | None = None, body: str = "", from_whatsapp: str | None = None) -> str:
        from_ = from_whatsapp or self.from_whatsapp
        to_ = to_number or self.to_whatsapp
        
        try:
            message = self.client.messages.create(
                from_=from_,
                to=to_,
                body=body
            )
            return message.sid
        except Exception as e:
            print(f"Erro ao enviar mensagem pelo Twilio: {e}")
            raise HTTPException(status_code=500, detail="Erro ao enviar mensagem via Twilio")

        
    def enviar_menu_interativo(self, telefone_cliente: str | None = None, telefone_empresa: str | None = None):
        from_ = f"whatsapp:{telefone_empresa or self.from_whatsapp}"
        to_ = f"whatsapp:{telefone_cliente or self.to_whatsapp}"

        interactive = {
            "type": "button",
            "body": {"text": "Olá! Como posso ajudar? Escolha uma opção:"},
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": "marcar_agenda", "title": "Marcar agenda"}},
                    {"type": "reply", "reply": {"id": "duvidas", "title": "Falar sobre outro assunto (dúvidas)"}}
                ]
            }
        }

        try:
            message = self.client.messages.create(
                from_=from_,
                to=to_,
                interactive=interactive
            )
            return {"success": True, "sid": message.sid}

        except Exception as e:
            print(f"Erro ao enviar menu interativo: {e}")
            return {"success": False, "error": str(e)}



        