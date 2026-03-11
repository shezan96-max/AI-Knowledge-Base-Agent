import requests
from app.config import BREVO_API_KEY,SENDER_EMAIL
#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart

def send_email(to_email,subject,body):
    url = "https://api.brevo.com/v3/smtp/email"
    

    headers = {
        "accept" : "application/json",
        "api-key" : BREVO_API_KEY,
        "content-type" : "application/json"
    }

    payload = {
        "sender" : {"email" : SENDER_EMAIL},
        "to" : [{"email" : to_email}],
        "subject" : subject,
        "textContent" : body
    }

    response = requests.post(url=url,headers=headers,json=payload,timeout=10)

    print(response.status_code)
    print(response.text)

    if response.status_code not in [200,201]:
        raise Exception("Email sending failed")


    '''# SMTP version
    sender_email = SENDER_EMAIL
    app_password = APP_PASSWORD

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body,"plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com",578)
        server.starttls()

        server.login(sender_email,app_password)

        server.sendmail(sender_email,to_email,msg.as_string())
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Error:",e)'''
        





















    