import os
from typing import Tuple
from dotenv import load_dotenv
from langchain_core.prompts import (
    PromptTemplate,
)  # PromptTemplate is a template for creating prompts
from langchain_openai import (
    ChatOpenAI,
)  # ChatOpenAI is a class for interacting with OpenAI's chat models
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import (
    StrOutputParser,
)  # StrOutputParser is used to parse string outputs
from third_parties.linkedin import scrap_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import (
    summary_parser,
    Summary,
)  # Importing the summary parser for output formatting


def ice_break_with(name: str) -> Tuple[Summary, str | None]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrap_linkedin_profile(linkedin_url=linkedin_username, mock=True)

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary of their professional background and expertise.
    2. two interesting facts about them.\n
    {format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOllama(model="gemma3:1b", temperature=0)

    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from a .env file
    # print("Hello, World!")

    print(
        ice_break_with(name="Youssef Shehata MegaSoft LinkedIn")
    )  # Call the ice_break_with function with a name
