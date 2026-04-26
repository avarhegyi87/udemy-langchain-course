from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
import os

from dotenv import load_dotenv
from langchain.messages import HumanMessage

load_dotenv()


tavily = TavilyClient()


@tool
def search(query: str):
    """
    Tool that searches on the internet
    Args:
        query: The query to search
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from udemy-langchain-course!")
    for env_name in ["OPENAI_API_KEY", "LANGSMITH_API_KEY", "TAVILY_API_KEY"]:
        if not os.getenv(env_name):
            raise ValueError(f"{env_name} is not set")
    print("All API keys loaded successfully")

    result = agent.invoke(input={"messages": HumanMessage(
        content="Search for 3 job postings on LinkedIn or nofluffjobs.com for developer using langchain in Budapest, Hungary and list their details")})
    print(result)


if __name__ == "__main__":
    main()
