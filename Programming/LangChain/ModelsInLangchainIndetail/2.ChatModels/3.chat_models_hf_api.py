# See this video - https://youtu.be/HdcLE8JuMrA?si=NkW65685x2JMFJtz&t=3207

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
# load_dotenv()

# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello."},
# ]

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens = 77
)
model = ChatHuggingFace(llm=llm)

result = model.invoke ("What is LangChain?")
print(result.content)

# for chunk in model.stream(messages):
#         print(chunk.content, end="", flush=True) 