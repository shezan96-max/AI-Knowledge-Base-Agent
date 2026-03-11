from dotenv import load_dotenv
import os

load_dotenv()

BREVO_API_KEY=os.getenv("BREVO_API_KEY")
SENDER_EMAIL=os.getenv("SENDER_EMAIL")
#APP_PASSWORD=os.getenv("APP_PASSWORD")
ADMIN_EMAIL=os.getenv("ADMIN_EMAIL")