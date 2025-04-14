from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a detailed report on - {report}',
    input_variables=['report']
)

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'Write 5 line summary of the following text. \n {text} and mark each line with number',
    input_variables=['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser

print(chain.invoke('topic: BlackHole'))

chain.get_graph().print_ascii()