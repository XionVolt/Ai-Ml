from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


# schema
class StructuredOutput(TypedDict):
    summary: str
    sentiment: float

structured_model = model.with_structured_output(StructuredOutput)



result = structured_model.invoke("""The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated
compared to other brands. Hoping for a software update to fix this.""")

print('Structured Output in python dictionary:')
print(result)

print('summary:')
print(result['summary'])

print('sentiment:')
print(result['sentiment'])

# How its all happening😀🤔 -> https://youtu.be/y5EmRr1O1h4?si=o-yBNKRSZ32Tqayn&t=1505


## Annotated TypedDict
""" class AnnotatedStructuredOutput(TypedDict):
        summary: Annotated[str, "Summary of the text"]
        sentiment: Annotated[str, "Return sentiment of the review either negative,positive or neutral"]
    

annotated_structured_model = model.with_structured_output(AnnotatedStructuredOutput)

 """