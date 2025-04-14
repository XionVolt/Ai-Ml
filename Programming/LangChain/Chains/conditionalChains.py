from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Initialize model and parsers
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
parser = StrOutputParser()

# Define output schema using Pydantic
class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(description="Sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt to classify sentiment
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative:\n{feedback}\n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)

# Create the classifier chain
raw_classifier_chain = prompt1 | model | parser2

# Wrap the sentiment output with original feedback text
classifier_chain = RunnableLambda(
    lambda feedback: {
        "feedback": feedback,
        "sentiment": raw_classifier_chain.invoke(feedback).sentiment
    }
)

# Prompt for positive feedback response
prompt2 = PromptTemplate(
    template="""
You are writing a response that will be sent directly to a customer who gave positive feedback.
Use only the details from the feedback to write a genuine, thoughtful, and complete response.

Do not use any placeholders like [Product Name] or [Company Name]. The response should sound human and appreciative.

Here is the customer feedback:
"{feedback}"

Write a polished response to thank them sincerely.
""",
    input_variables=["feedback"]
)


# Prompt for negative feedback response
prompt3 = PromptTemplate(
    template="""
You are writing a response that will be sent directly to a customer who gave negative feedback.
Use only the details from the feedback to write a sincere and polite response.

Do not use any placeholders like [Product Name] or [Company Name]. Acknowledge their concerns genuinely and show that we care.

Here is the customer feedback:
"{feedback}"

Write a professional and empathetic response addressing their concerns.
""",
    input_variables=["feedback"]
)


# Conditional branching based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "Positive", prompt2 | model | parser),
    (lambda x: x["sentiment"] == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda _: "Could not determine sentiment.")
)

"""
Here:  prompt2 and prompt3 receive the full dictionary {"feedback": ..., "sentiment": ...}, but thanks to PromptTemplate that it will consider "feedback" only as we specified "feedback" in `input_variables` specifically.`, and thus it ignore extra keys in dictionary , here `sentiment`.
"""

# Full chain: classify → branch
chain = classifier_chain | branch_chain

# Test it
print(chain.invoke("I love this product"))

# Optional: visualize graph
chain.get_graph().print_ascii()