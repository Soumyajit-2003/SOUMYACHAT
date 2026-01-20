from click import prompt
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from src.agents.chat_agent.tools.date_time import get_current_datetime
from src.agents.chat_agent.tools.web_search_tool import search_the_web


template = """You are a helpful AI assistant. give detailed and proper structured answers to user queries 
Message History: {message_history}"""

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"

def chat(state: ChatAgentState) -> ChatAgentState:
    """"""
    prompt_template = ChatPromptTemplate.from_template(template = template)
    model = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=GROQ_API_KEY,
    )
    model = model.bind_tools(
        [
            get_current_datetime, search_the_web
        ]
    )
    chain = prompt_template | model
    answer = chain.invoke(state["message"])
    return {"message": [answer]}
