from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from PUBLIC_VARIABLES import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

PERSIST = r"app\utils\data\langchainModel"
embedding = OpenAIEmbeddings()
VECTOR_DB = Chroma(persist_directory=PERSIST, embedding_function=embedding)
QA = VectorDBQA.from_chain_type(
    llm=OpenAI(), chain_type="stuff", vectorstore=VECTOR_DB)


class JordanGpt:
    def __init__(self):
        self.model = QA
        self.prompt = "Keep the conversation relevent to information about Jordan Eisenman. Redirect questions to be about Jordan."

    def query(self, query):
        return self.model.run(query)


JORDAN_GPT = JordanGpt()
# JORDAN_GPT.query("What is something in this document?")
