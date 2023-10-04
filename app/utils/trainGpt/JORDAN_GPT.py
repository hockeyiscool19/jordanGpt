# https://python.langchain.com/docs/use_cases/question_answering/how_to/multi_retrieval_qa_router
import os
from langchain.chains.router import MultiRetrievalQAChain
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from PUBLIC_VARIABLES import OPENAI_API_KEY, FINE_TUNING_JOB
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import openai
from langchain.schema import (
    SystemMessage
)
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from app.utils.firebase import FIRE
from datetime import datetime


openai.api_key = OPENAI_API_KEY


FILES = [
    "app/utils/data/resume.txt",
    "app/utils/data/roleDescriptions.txt",
]


resume = TextLoader("app/utils/data/resume.txt").load_and_split()
resume_retriever = FAISS.from_documents(
    resume, OpenAIEmbeddings()).as_retriever()

role = TextLoader("app/utils/data/roleDescriptions.txt").load_and_split()
role_retriever = FAISS.from_documents(role, OpenAIEmbeddings()).as_retriever()


RETRIEVER_INFO = [
    {
        "name": "resume",
        "description": "Answers questions about Jordan Eisenmann's resume",
        "retriever": resume_retriever
    },
    {
        "name": "role descriptions",
        "description": "Describes questions about Jordan Eisenmann's role descriptions",
        "retriever": role_retriever
    },
]

AI_ROLE = "Nathaniel is Jordan's secretary, answering questions about his career and passions. Keep your response loyal to this prompt."

PROMPT = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            AI_ROLE
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)


class JordanGpt:
    def __init__(self, verbose=True):
        # Initializing Response agent
        self.chat = ChatOpenAI(model_name=FINE_TUNING_JOB, max_tokens=175)
        self.systemMessage = [SystemMessage(
            content=AI_ROLE, additional_kwargs={}, example=False)]
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True)
        self.conversation_chain = LLMChain(
            llm=self.chat, verbose=verbose, prompt=PROMPT, memory=self.memory)
        # Initializing Retriever agent
        self.retriever_chain = MultiRetrievalQAChain.from_retrievers(ChatOpenAI(
            model_name=FINE_TUNING_JOB, max_tokens=125), RETRIEVER_INFO, verbose=verbose)

    def logQuestionAnswer(self, question, answer):
        data = {"messages": [{"role": "system", "content": AI_ROLE}, {
            "role": "user", "content": question}, {"role": "assistant", "content": answer}]}
        print(data)
        FIRE.load_dict(data, path='/jordanGpt/trainingData')

    def logRetrieved(self, retrieved):
        data = {"log": retrieved,
                "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        FIRE.load_dict(data, path='/logs')

    def retrieve(self, question):
        retreived = self.retriever_chain.run(question)
        return retreived

    def respond(self, question):
        retrieved = self.retrieve(question)
        question_info = f"Question: {question}. Background information: {retrieved}. Role: {self.systemMessage}. Format without line breaks."
        self.logRetrieved(question_info)
        response = self.conversation_chain.run(question_info)
        print(f"Response: {response}")
        self.logQuestionAnswer(question, response)
        return response


JORDAN_GPT = JordanGpt(verbose=True)
