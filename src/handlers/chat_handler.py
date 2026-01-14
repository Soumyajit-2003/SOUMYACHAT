from src.agents.chat_agent.graph import create_chat_agent_graph
from langchain.messages import HumanMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

graph = create_chat_agent_graph()


def chat_agent_handler(message: str) -> ChatAgentState:
    """ """

    return graph.invoke({"message": [HumanMessage(content=message)]})
