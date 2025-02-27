# pip3 install langchain langchain-community langchain-openai 
# pip3 install python-dotenv

from Models.ProjectIdeaRequest import ProjectIdeaRequest
from Models.ProjectIdeaResponse import ProjectIdeaResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post("/")
async def generateIdeaAsync(ideaRequest: ProjectIdeaRequest):
    print("Entered generateIdeaAsync")
    llm = setupChatConnectionWithOpenAi()
    promptTemplate = getPromptTemplate()
    rag_chain = (
        {"level": RunnablePassthrough(), "prompt": RunnablePassthrough()} |
        promptTemplate |
        llm.with_structured_output(ProjectIdeaResponse)
    )
    print("sending request")
    response = rag_chain.invoke({"level": ideaRequest.Level, "prompt": ideaRequest.Prompt})
    print("returning response")
    return response

PROMPT_TEMPLATE = """
You are a project idea generator. Your task is to take the prompt from the user and the skill level.
You need to return A project title, tools and knowledge required and also a description giving high 
level idea of what the endproduct of the project should be.
-------
If you cannot think of an idea or any other details, just say so. 
DO NOT GIVE IRREVANT INFO.
-------
Now generate an idea and give other info based on the following:
Level: {level}
Prompt: {prompt}

"""

def getPromptTemplate() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

def setupChatConnectionWithOpenAi() -> ChatOpenAI:
    load_dotenv()
    return ChatOpenAI(model = "gpt-4o-mini")

