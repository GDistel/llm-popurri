from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

model = ChatOpenAI()
parser = StrOutputParser()
chain = prompt_template | model | parser

def translate(text: str, language: str) -> str:
    return chain.invoke({"language": language, "text": text})
