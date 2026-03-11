from fastapi import APIRouter
from app.database.connection import get_connection

router = APIRouter()

@router.get("/analytics")
def get_analytics():

    conn = get_connection()
    cursor = conn.cursor()

    # Total Converstaions
    cursor.execute("SELECT COUNT(*) FROM conversations")

    total_conversations = cursor.fetchone()[0]

    # Total Leads 
    cursor.execute("SELECT COUNT(*) FROM leads")
    total_leads = cursor.fetchone()[0]

    # Intent Breakdown
    cursor.execute("""
        SELECT intent, COUNT(*)
        FROM leads
        GROUP BY intent

""")
    intent_data = cursor.fetchall()

    intents = {intent : count for intent, count in intent_data}

    cursor.close()
    conn.close()

    return {
        "total_conversations": total_conversations,
        "total_leads" : total_leads,
        "lead_intents" : intents
    }