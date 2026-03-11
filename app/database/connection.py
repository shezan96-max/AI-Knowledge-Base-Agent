import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="chatbot_db",
        user="postgres",
        password="B2B-Billionaire$$"
    )

    return conn