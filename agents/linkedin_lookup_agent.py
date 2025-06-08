import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOllama(model="qwen3:0.6b", temperature=0)
    template = """/no_think given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page by searching google for it first.
                              Your answer should contain only the LinkedIn URL."""
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page url",
            func=get_profile_url_tavily,
            description="Useful for looking up a person's LinkedIn profile URL by their name and the company if needed. The input should be a string containing the person's name and optionally the company they work for. The output will be a URL to their LinkedIn profile page.",
        )
    ]

    # add the /no_think prompt to the react prompt pulled from the hub
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    agent_executor = AgentExecutor(
        agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format(name_of_person=name)}
    )

    linkedin_url = result["output"]
    return linkedin_url


if __name__ == "__main__":
    linkedin_url = lookup("Youssef Shehata MegaSoft LinkedIn")
    print(linkedin_url)
