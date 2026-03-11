from fastapi import APIRouter
from app.api.schemas.ask_schema import AgentRequest,AgentResponse
from app.core.rag import load_knowledge_base,run_rag
from app.services.intent import detect_intent
from app.database.conversation_db import save_conversation
from app.database.lead_db import save_lead
from app.automation.workflow import trigger_workflow

router = APIRouter()

@router.post("/ask",response_model=AgentResponse)
def ask(request : AgentRequest):
    store = load_knowledge_base()
    
    email = request.email
    question = request.question

    answer = run_rag(question,store)
    intent = detect_intent(question)

    save_conversation(email,question,answer)

    save_lead(email,question,intent)

    trigger_workflow(intent,email)

    return AgentResponse(answer=answer)



