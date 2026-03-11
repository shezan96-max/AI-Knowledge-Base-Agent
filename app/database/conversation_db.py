from app.database.connection import get_connection

def save_conversation(email,question,answer):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO conversations (email,question,answer)
        VALUES (%s,%s,%s)
    """

    cursor.execute(query, (email,question,answer))
    conn.commit()
    cursor.close()
    conn.close()
    print("Conversation saved to DB")
    