import os
from typing import TypedDict, Annotated, Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import uvicorn
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5, api_key=GEMINI_API_KEY)



#API Endpoints
@app.get("/")
async def root():
    return {
        "message": "LangGraph RAG API",
    }

@app.get("/test")
async def test():
    return {
        "message": "Testing LangGraph RAG API",
    }


### Run 
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000