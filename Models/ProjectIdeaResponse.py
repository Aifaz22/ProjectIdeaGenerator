from pydantic import BaseModel, Field

class ProjectIdeaResponse(BaseModel):
    ProjectTitle: str = Field(description='The title of the project')
    ProjectToolsAndKnowledgeRequired: str = Field(description='The tools and knowledge needed to complete the project')
    ProjectIdeaDescription: str = Field(description='The description and details about the project')
    IdeaReasoning: str = Field(description="Give your reasoning why this is the best idea you thought")
