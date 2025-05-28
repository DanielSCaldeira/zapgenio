from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import PlainTextResponse
from backend.services.integracao.twilio_service import TwilioService


router = APIRouter()

@router.get("/")
async def check_whatsapp():
    return {"status": "Webhook Twilio GET ativo"}

@router.post("/mensagem_recebida", response_class=PlainTextResponse)
async def mensagem_recebida(
    request: Request,
    twilio_service: TwilioService = Depends(TwilioService)
):
    form = await request.form()
    from_number = form.get("From")
    body = form.get("Body")

    if not from_number or not body:
        return PlainTextResponse("Dados inválidos recebidos", status_code=400)

    print(f"📨 Mensagem recebida de {from_number}: {body}")

    # Envia menu interativo de resposta (ajuste conforme sua lógica)
    twilio_service.enviar_menu_interativo(telefone_cliente=from_number)

    return PlainTextResponse("Mensagem recebida com sucesso", status_code=200)


@router.post("/enviar_mensagem", response_class=PlainTextResponse)
async def enviar_mensagem(
    from_number: str = Form(...),
    twilio_service: TwilioService = Depends(TwilioService)
):
    try:
        twilio_service.enviar_mensagem(
            to_number=from_number,
            body="Olá! Recebemos sua mensagem no ZapGênio. ✅"
        )
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        return PlainTextResponse("Erro interno ao processar", status_code=500)

    return PlainTextResponse("Mensagem enviada com sucesso", status_code=200)
