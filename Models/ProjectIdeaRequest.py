from pydantic import BaseModel

class ProjectIdeaRequest(BaseModel):
    Prompt: str
    Level: str