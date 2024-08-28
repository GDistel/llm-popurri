import os
from langchain_community.utilities import SQLDatabase
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableLambda

from app.helpers import clean_sql_query_fn

llm = ChatOpenAI(model="gpt-4o-mini")

answer_prompt = PromptTemplate.from_template(
    """
    Given the following user question, corresponding SQL query, and SQL result, answer the user question.

    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: 
    """
)

DB_URI = os.environ.get('POSTGRES_DB_URL')

if (DB_URI is None):
    raise Exception("The POSTGRES_DB_URL must be set as an environment variable")

db = SQLDatabase.from_uri(DB_URI)

write_query = create_sql_query_chain(llm, db)
execute_query = QuerySQLDataBaseTool(db=db)

chain = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | RunnableLambda(clean_sql_query_fn) | execute_query
    )
    | answer_prompt
    | llm
    | StrOutputParser()
)

def ask_question_to_db(question: str) -> str:
    return chain.invoke({"question": question})