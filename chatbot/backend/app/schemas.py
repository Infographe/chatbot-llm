from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --------------------------------------------------
# Modèles Pydantic
# --------------------------------------------------
class UserProfile(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    objective: str
    level: str
    knowledge: str
    pdf_content: Optional[str] = None
    recommended_course: Optional[str] = None

# Ajout d'un modèle ChatMessage
class ChatMessage(BaseModel):
    role: str  # 'user' ou 'assistant'
    content: str

class SendEmailRequest(BaseModel):
    profile: UserProfile
    chatHistory: List[ChatMessage] = []

class RecommendRequest(BaseModel):
    profile: UserProfile

class RecommendResponse(BaseModel):
    recommended_course: str
    reply: str
    details: Optional[dict] = None

class QueryRequest(BaseModel):
    profile: UserProfile
    history: List[ChatMessage] = [] #modifié pour correspondre à la structure de ChatMessage , avant :   history: List[dict] = []
    question: str

class QueryResponse(BaseModel):
    reply: str