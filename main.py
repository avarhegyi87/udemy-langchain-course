import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from udemy-langchain-course!")
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set")
    else:
        print("All API keys loaded successfully")

    information = """
    Arvind Krishna (born November 23, 1962)[2] is an Indian-American business executive, and the chairman and CEO of IBM. He has been CEO of IBM since April 2020 and chairman since January 2021.[3][4] Krishna began his career at IBM in 1990, at its Thomas J. Watson Research Center,[5] and was promoted to senior vice president in 2015, managing IBM Cloud & Cognitive Software and IBM Research divisions. He was a principal architect of the acquisition of Red Hat, the largest acquisition in the company's history.[6][7]

Early life and education
Krishna was born in a Telugu family in West Godavari District, Andhra Pradesh, India.[1][8][9] His father, Major General Vinod Krishna, was an army officer who served in the Indian Army and his mother, Aarathi Krishna, worked for the welfare of Army widows.[10][11] Krishna studied at Stanes Anglo Indian Higher Secondary School in Coonoor, Tamil Nadu, and at St Joseph's Academy, Dehradun.[12]

Krishna received a Bachelor of Technology degree in electrical engineering from Indian Institute of Technology, Kanpur in 1985 and a Doctor of Philosophy in electrical engineering from the University of Illinois Urbana-Champaign in 1991.[13][14][15][16]

Career
Professional career
Krishna joined IBM's Thomas J. Watson Research Center in 1990, and continued in Watson Research for 18 years until 2009. Thereafter, he held a General Manager role in Information management software and systems and technology group of IBM. In 2015, he was promoted to senior vice president of IBM Research.[17] He later became senior vice president of IBM's cloud and cognitive software division.[8]

Krishna also led the building and expansion of new markets for IBM in artificial intelligence, cloud, quantum computing, and blockchain technology.[18][19] He was a driving force behind IBM's $34 billion acquisition of Red Hat, which closed in July 2019.[20]

He was appointed IBM's CEO in January 2020, effective April 6, 2020,[21] succeeding Ginni Rometty who was CEO since 2012.[22] He joined Satya Nadella, Shantanu Narayen, and Sundar Pichai as an Indian-American CEO of a major United States technology company.[23][24] In 2021, he was named by CRN as the year's "Most Influential Executive".[25]

Krishna is a member of The Business Council.[26]

Research
Krishna has co-authored 15 patents, has been the editor of IEEE and ACM journals, and has published extensively in technical journals.[27]
    """

    summary_template = f"""
    Given the information {information} about a person I want you to create:
    1. a short summary
    2. interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    model = 'gpt'
    if model == 'gpt':
        llm = ChatOpenAI(temperature=0, model="gpt-5")
    else:
        llm = ChatOllama(temperature=0, model='gemma3:270m')
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
