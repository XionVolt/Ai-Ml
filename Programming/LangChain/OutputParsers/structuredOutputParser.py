from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from  langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic",type="string"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic",type="string"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic",type="string") # default type is also string
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':"BlackHole"})
# print(prompt)
# Ouptut

""" text='Give 3 fact about the BlackHole \n The output should be a markdown code snippet formatted in the following schema, 
including the leading and trailing "```json" and "```":\n\n```json\n{\n\t"fact_1": string  // fact 1 about the topic\n\t"fact_2": string  
fact 2 about the topic\n\t"fact_3": string  // fact 3 about the topic\n}\n```  """

chain = template | model | parser
print(chain.invoke({"topic":'BlackHole'}))