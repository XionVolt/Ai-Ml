from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = 'Write a detailed report on - {report}',
    input_variables=['report']
)

chain = prompt | ChatGoogleGenerativeAI(model="gemini-1.5-pro") | StrOutputParser()

# print(chain.invoke('topic: BlackHole')) 
chain.get_graph().print_ascii()