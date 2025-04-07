from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
# Define JSON schema
review_schema = {
    # This line (`$schema`) declares the version of JSON Schema you are using — in this case, Draft 7, which is one of the most commonly supported and stable versions.
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Review",
    "type": "object",  
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Key themes discussed in the review"
        },
        "summary": {
            "type": "string",
            "description": "Summary of the text"
        },
        "sentiment": {
            "type": "string",
            "enum": ["negative", "positive", "neutral"],
            "description": "Sentiment of the review"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "Pros mentioned in the review"
        },
        "cons": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "Cons mentioned in the review"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}

# Initialize the Ollama model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Use the JSON schema directly
structured_model = model.with_structured_output(schema=review_schema, method="json_mode")

# Sample input
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

# Invoke the structured output model
response = structured_model.invoke(input_text)

# Display output
print(response)
