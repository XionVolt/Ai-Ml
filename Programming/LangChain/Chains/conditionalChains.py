from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(description="Give the sentiment of the feedback")
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative:\n{feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)


# classify the sentiment of the following feedback text into positive or negative
classifier_chain = prompt1 | model | parser2

# print(classifier_chain.invoke("I love this product").sentiment) # Positive, so because of PydanticOutputParser, its assuring we get output in python dict


# Now we have to make branching(conditional) part 

prompt2 = PromptTemplate(
    template="Write an appropriate response for this positive feedback text:\n{feedback}, and this feedback will be sent to customer, so write pretty neat output for the customer",
)

prompt3 = PromptTemplate(
    template="Write an appropriate response for this negative feedback text:\n{feedback}, and this feedback will be sent to customer, so write pretty neat output for the customer",

)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
   RunnableLambda( lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke("I love this product"))

chain.get_graph().print_ascii()