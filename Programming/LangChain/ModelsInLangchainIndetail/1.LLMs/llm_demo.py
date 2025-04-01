#! D:\AiMl\Programming\LangChain\ModelsInLangchainIndetail\venv\Scripts\python.exe


from langchain_community.llms import Ollama

# Load a local LLM (like Mistral or Llama)
llm = Ollama(model="llama3.2")  # Change to "llama2" or other models if needed

# Generate a response
response = llm.invoke("What is LangChain?") # response = llm("What is LangChain?")  # Uses __call__()

""" 
The invoke method in LangChain is used to send a prompt to an LLM (or chain) and get a response.
It is the recommended way to interact with an LLM because it supports structured input and better integration.
"""

# print("LLM Response:", response)

# for stream
for chunk in llm.stream("What is LangChain?"):
    print(chunk, end="", flush=True)  

# Another Example to interact with llm of openai - https://youtu.be/HdcLE8JuMrA?si=afN_eEDxX5ZGqZQH&t=1247 