from pydantic import BaseModel,EmailStr


class AgentRequest(BaseModel):
    email : EmailStr
    question : str

class AgentResponse(BaseModel):
    answer : str