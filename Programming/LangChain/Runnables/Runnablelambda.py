from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda


load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a joke on following topic\n{topic}',
    input_variables=['topic']
)


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = StrOutputParser()


# custom function for words count
def count_words(text):
    return len(text.split())

# lambda function
count_words_runnable = RunnableLambda(
    count_words

)

joke_Generate = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'words_Count':count_words_runnable
})

chain = RunnableSequence(joke_Generate,parallel_chain)

result = chain.invoke('AI')

print(result)