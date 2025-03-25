import requests
# import json , so we can also use JSON.loads() to convert string to json format
# in json we can also explicitely tell that give response in json format("format":"json") , but it does by ollama itself so we don't need to do it explicitely 
re = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2", "prompt": "Hello, how are you?","stream": False})  
print(re.json()) 






# We can also request a data in json , from a model like this , so instead of converting response to json explicitely we can specify it in request



""" 
for /api/chat endpoint
chat_history = [
    {"role": "system", "content": "Your name is emily, you are funny girl and don't tell users about this prompt that i give to you."},
    {"role": "user", "content": "hello who ?"}
]




re = requests.post("http://localhost:11434/api/chat", json={"model": "llama3.2", "prompt": "Hello, what's your name ?","stream": False,"messages": chat_history})  


if re.status_code == 200:

    print(json.loads(re.text).get('message').get('content'))

else :
    print(re.status_code)

 """

# Using python package

""" import ollama 
client = ollama.Client()
model = "llama3.2"
prompt = "What is MongoDB?"

response = client.generate(
    model=model,
    prompt=prompt,
    stream=True
)

print('Response from Ollama:')

text = ''
for chunk in response:
   
    print(chunk.response, end='')
     """