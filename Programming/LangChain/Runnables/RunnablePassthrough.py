from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a joke on the following topic\n{topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain following joke\n{joke}',
    input_variables=['joke']
)

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = StrOutputParser()

jokeGenrate = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'JokeExplanation':RunnableSequence(prompt2,model,parser)
})

chain = RunnableSequence(jokeGenrate,parallel_chain)

result = chain.invoke('Chuck Norris')

print(f'{result["Joke"]}\n\n{result["JokeExplanation"]}')
