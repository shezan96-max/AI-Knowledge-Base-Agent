from app.automation.email import send_email
from app.config import ADMIN_EMAIL

def trigger_workflow(intent,email):
    if intent == "lead":
        subject = "🔥New Lead Received🔥"

        body = f"""
            A new lead has contacted through the AI Agent.

            User Email : {email}

            Please follow up with this customer.

            Best Regards,
            🤖Agent Supremo🤖

        """
        send_email(ADMIN_EMAIL,subject,body)

    elif intent == "demo":
        subject = "📆Demo Request Received📆"

        body = f"""
            A user requested a demo through the AI Agent.

            User Email : {email}

            Please schedule a demo with this user.

            Best Regards,
            🤖Agent Supremo🤖

        """
        send_email(ADMIN_EMAIL,subject,body)

    elif intent == "pricing":
        subject = "💰Pricing Inquiry💰"

        body = f"""
            A user asked about pricing.

            User Email : {email}

            Consider sending pricing details.

            Best Regards,
            🤖Agent Supremo🤖

        """
        send_email(ADMIN_EMAIL,subject,body)

    else:
        pass