from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


# schema using Pydantic
class StructuredOutput(BaseModel):
    summary: str
    sentiment: str = Field(description="Sentiment of the review, positive, negative or neutral")

structured_model = model.with_structured_output(StructuredOutput)

result = structured_model.invoke("""The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated
compared to other brands. Hoping for a software update to fix this""")

print('Structured Output in python dictionary:')
print(result.dict())  # Convert Pydantic model to dictionary

print('summary:')
print(result.summary)

print('sentiment:')
print(result.sentiment)

# How its all happening😀🤔 -> https://youtu.be/y5EmRr1O1h4?si=o-yBNKRSZ32Tqayn&t=1505