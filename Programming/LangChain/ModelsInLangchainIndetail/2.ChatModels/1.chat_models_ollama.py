# See this video to see how to interact with chat models - https://youtu.be/HdcLE8JuMrA?si=QZtOiYmDTKfWoFgp&t=1877

from langchain_community.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Load a local chat model (like Llama3 or Mistral)
# you can pass any parameters to chat model like `temperature` , `max_completion_tokens` , etc ...
chat_model = ChatOllama(model="llama3.2",temperature=1)  # Change to other models if needed, more guide on temperature -  https://youtu.be/HdcLE8JuMrA?si=AkseXwOQluESPOxl&t=2307

# Creating a chat history
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain."),
]

# Get response from chat model

# response = chat_model.invoke(messages)
# print("Chat Model Response:", response.content)

# Streaming response
def stream_response():
    for chunk in chat_model.stream(messages):
        print(chunk.content, end="", flush=True)  # Streams the response live

print("\nStreaming Response:")
stream_response()


# 