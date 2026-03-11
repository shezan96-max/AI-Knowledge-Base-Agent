from fastapi import UploadFile, File, APIRouter
import os
import shutil

from app.core.rag import build_knowledge_base

router = APIRouter()

@router.post("/upload-knowledge")
async def upload_knowledge(file : UploadFile = File(...)):

    upload_dir = "data"
    os.makedirs(upload_dir,exist_ok=True)

    file_path = os.path.join(upload_dir,file.filename)

    # If same file exists - delete
    if os.path.exists(file_path):
        os.remove(file_path)

    # Save uploaded file
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    # Rebuild knowledge base (this will create new FAISS index)
    build_knowledge_base(file_path)

    return {
        "message" : "Knowledge Base Updated",
        "file" : file.filename
    }