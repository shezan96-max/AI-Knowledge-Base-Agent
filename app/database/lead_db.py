from app.database.connection import get_connection

def save_lead(email,question,intent):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO leads (email,question,intent)
        VALUES (%s,%s,%s)
    """

    cursor.execute(query, (email,question,intent))
    conn.commit()

    cursor.close()
    conn.close()
    print("Lead saved to DB")
    