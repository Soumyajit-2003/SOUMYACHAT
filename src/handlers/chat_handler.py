from src.agents.chat_agent.graph import create_chat_agent_graph

graph = create_chat_agent_graph()


def chat_agent_handler(message: str) -> dict[str, str]:
    """Handle chat agent"""
    return graph.invoke({"message": message}) # {"messages": "Answer from chat agent"}
