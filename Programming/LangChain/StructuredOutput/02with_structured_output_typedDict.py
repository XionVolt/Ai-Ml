from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import List, Literal

# Define the output schema using Pydantic
class Review(BaseModel):
    key_themes: List[str] = Field(description="Key themes discussed in the review")
    summary: str = Field(description="Summary of the text")
    sentiment: Literal["negative", "positive", "neutral"] = Field(description="Sentiment of the review")
    pros: List[str] = Field(description="Pros mentioned in the review")
    cons: List[str] = Field(description="Cons mentioned in the review")

# Initialize the Ollama model
model = ChatOllama(model="llama3.2")

# Configure the model to use the JSON schema method for structured output
structured_model = model.with_structured_output(Review, method="json_schema")

# Input text
input_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
"""

# Invoke the model
response = structured_model.invoke(input_text)

# Output the structured response
print(response.json())
