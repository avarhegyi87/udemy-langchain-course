import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for an agent response"""

    answer: str = Field(description="The agent's answer to the query")
    sources: list[Source] = Field(
        default_factory=list,
        description="The list of sources used to generate the answer",
    )


llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from udemy-langchain-course!")
    for env_name in [
        "OPENAI_API_KEY",
        "LANGSMITH_API_KEY",
        "TAVILY_API_KEY",
    ]:
        if not os.getenv(env_name):
            raise ValueError(f"{env_name} is not set")
    print("All API keys loaded successfully")

    result = agent.invoke(
        input={
            "messages": HumanMessage(
                content="Search for 5 medior or senior job postings on LinkedIn or nofluffjobs.com for developer using langchain in Budapest, Hungary and list their details"
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
