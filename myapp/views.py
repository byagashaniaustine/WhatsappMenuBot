# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
import logging

# Use the "myapp" logger from settings.py
logger = logging.getLogger("myapp")
@csrf_exempt
def whatsapp_webhook(request):
    try:
        if request.method == "POST":
            incoming_msg = request.POST.get("Body", "").strip().lower()
            from_number = request.POST.get("From", "")
            logger.info(f"📩 Incoming WhatsApp message from {from_number}: {incoming_msg}")
            
            resp = MessagingResponse()
            # ... rest of your menu logic ...
            return HttpResponse(str(resp))
        return HttpResponse("OK")
    except Exception as e:
        logger.exception("Webhook failed:")
        return HttpResponse("Internal Server Error", status=500)


    # Menu options dictionary
    menu = {
        "1": (
            "📈 *Improving Credit Score Tips:*\n"
            "- Pay bills on time ✅\n"
            "- Keep credit usage below 30%\n"
            "- Limit applying for too many loans\n"
            "- Check your credit report regularly"
        ),
        "2": (
            "🏦 *Qualify for a Loan:*\n"
            "- Maintain a stable income source\n"
            "- Build a good repayment history\n"
            "- Reduce existing debt before applying\n"
            "- Prepare all required documents early"
        ),
        "3": (
            "💡 *Smart Debt Repayment:*\n"
            "- Pay more than the minimum if possible\n"
            "- Focus on high-interest debt first (avalanche method)\n"
            "- Avoid unnecessary new loans\n"
            "- Create a realistic repayment plan"
        ),
        "4": (
            "⚠️ *Common Mistakes to Avoid:*\n"
            "- Missing payment deadlines\n"
            "- Using all available credit\n"
            "- Taking too many short-term loans\n"
            "- Ignoring your credit report"
        ),
        "5": "☎️ Our financial coach will reach out to you soon!"
    }

    # MAIN MENU triggers
    if incoming_msg in ["hi", "hello", "start", "menu", ""]:
        resp.message(
            "👋 *Welcome to Credit/Loan Tips Bot!*\n"
            "💡 Choose a topic to learn about:\n\n"
            "1️⃣ How to improve your credit score\n"
            "2️⃣ How to qualify for a loan\n"
            "3️⃣ Smart ways to repay debt\n"
            "4️⃣ Avoiding common credit mistakes\n"
            "5️⃣ Talk to a financial coach"
        )
    # Respond to menu selections
    elif incoming_msg in menu:
        resp.message(menu[incoming_msg])
    # Handle invalid input
    else:
        resp.message(
            "🤔 I didn't get that. Please reply with *menu* to see the topics again."
        )

    # Log outgoing response
    logger.info(f"✉️ Sending response to {from_number}")

    return HttpResponse(str(resp))
