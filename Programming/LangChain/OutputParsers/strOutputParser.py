from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# 1st Prompt, detailed report on the topic
template1 = PromptTemplate(
    template = 'Write a detailed report on - {report}',
    input_variables=['report']
)

# 2nd Prompt, summarize report that come from response of 1st prompt

template2 = PromptTemplate(
    template = 'Write 5 line summary of the following text. \n {text} and mark each line with number',
    input_variables=['text']
)

# create parser
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

print(chain.invoke('topic: BlackHole'))

