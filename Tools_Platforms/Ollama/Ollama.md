# What is Ollama ?
Ollama is an open source tool that is designed to essentially simplify the process of running LLM locally meaning on your hardware. 
[Resource for learning about Ollama](https://youtu.be/GWB9ApTPTv4?si=t_BxY0x4EAc2cL6v)
- [But let's see first , what model is](https://youtu.be/2Pm93agyxx4?si=l13rVLeWJY14w-pM&t=188)
An AI model is a program trained on data to make its own decisions and predictions using new data without human intervention. It uses algorithms to find patterns and make predictions based on the data it has been trained on.<br>
A model can also be considered a collection of nodes that work together to process and analyze data
- Parameters can be thought of collection of weights of biases (basically parameters are the variables that model learn during the training process). Once the model is developed(means file) that file each parameter is represented by 16 to 32 bits 
    - So for example if model is ollama:8b means model has 8 billion params and each represented have precision of 32bit, then that model will take 4bytes(32/8 = 4bytes) * 8billion = 32gb of vram to run. 
      - But if we qunatized our parameter to 4bits, it will then roughly take 4 to 5gigabyte of vram require to run a model


- Ollama provides a straightforward way to download run and interact with various models or LLMs without us having to rely on cloud based services .

[What problems ollama solves ?](https://youtu.be/GWB9ApTPTv4?si=ST0YqXhx07bcZY4s&t=530)

[Key features of ollama](https://youtu.be/GWB9ApTPTv4?si=Uu-sYk4eWQq3iQDn&t=793)

[Use Cases of ollama](https://youtu.be/GWB9ApTPTv4?si=EiLQjHFcD4VaT0s8)

[Different commands](https://youtu.be/GWB9ApTPTv4?si=z8TBayoeUjy0cfIT&t=1440)

-  `ollama run model`:numB , to download model with specific parameters
- ollama list : to list all models that you downloaded

[Understand the things that `/show info` shows](https://youtu.be/GWB9ApTPTv4?si=MEEWcRP0sVfsseUp&t=2053)
- **Model parameters** are variables that the model learns during the training process to make predictions or decisions. These parameters include weights and biases in neural networks, which are adjusted to minimize prediction errors and improve the model's performance.
  - Model parameters can be used to measure the complexity of model , and capacity of the model to learn from the data .
  - [Embedding length](https://youtu.be/GWB9ApTPTv4?si=slOB4oSe9EvbezMF&t=2291)
  - [Quantization](https://youtu.be/2Pm93agyxx4?si=OkesFUzR0zhbGsul&t=236)
      - [Quantization in short](https://youtu.be/GWB9ApTPTv4?si=YrUXLirO6dgbQjeg&t=2367)

- ***Context window***(or context size) - A ***context window*** in large language models (LLMs) **is the maximum number of tokens the model can process at once**, acting as its short-term memory capacity.
 This window determines how much information the model can consider when generating responses, impacting its ability to produce coherent and contextually relevant outputs.
 Larger context windows allow for more extensive inputs, enhancing the model's performance in tasks that require understanding of the full context, such as in-context learning.
 However, increasing the context window size also introduces challenges like higher computational demands and maintaining accuracy over longer text spans.

   - By default, Ollama models operate with a context window size of 2048 tokens.
This setting can be adjusted to accommodate more extensive input data, which is particularly useful for complex queries or when handling larger datasets.2048 tokens means if your input goes larger than 2048 tokens, the model will start to forget the previous tokens and will start to generate the response based on the new tokens.

[Some more Ollama Commands](https://youtu.be/GWB9ApTPTv4?si=jSiB47IfJ8oRa8iN&t=2640)


- [We can also modify or we can say customize our model](https://youtu.be/GWB9ApTPTv4?si=gZ2JxzTaqqTRKC4J&t=3240) because we can add certain pieces of metadata to the model to what we want it to be . 
- Temperature in context of Model : Temperature is what allows the model to be more creative , more direct ..., More detailed explanation is in separate targeted file . 
- Basically we can also set different parameters for our Ml Model in separate file , for customize(fine tune) the model according to our needs
ModelFile explained in detail in separatefile named `modefile-customizeModel.md`

- Run this command to see modelfile of your llm
```powershell
ollama show --modelfile  <model-name>
````



ollama serve at some end point locally , and it all serve at localhost:11434 , that means we can generate the response using rest Api

[See this clip](https://youtu.be/yPphKQp1fqE?si=2UHUGvkoK7Yx4kPw&t=907)

So we can generate response using rest api , we have two endpoints for making request to ollama , one is `api/generate` and other is `api/chat`


```bash
curl http://localhost:11434/api/generate -d '{ "model":"llama3.2"
"prompt":"Hello, how are you?" ,}' 
```

For powershell
```bash 
curl -Uri "http://localhost:11434/api/generate" -Method Post -Body 
'{ "model": "llama3.2", "prompt": "Hello, how are you?" }' -ContentType "application/json"

```
[stream flag](https://youtu.be/GWB9ApTPTv4?si=KK8GKKFw-lXte-Ei&t=3709) - basically this flag waits for whole response to be comes before display the response , its just that parameter that we seen in python `request` library




python can also be used for sending the request to llm and get response



```python
import requests
import json
re = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2", "prompt": "Hello, how are you?","stream": False})  """ Ollama supports 
"stream": False" in the JSON payload, 
which makes it return the full response at once. 
 So we have to assign stream flag to False in 
 payload instead of requests.post parameter , because 
in our case, Ollama's /api/generate returns a streaming response by default, so even if you set stream=False in parameter, 
it won't work as ollama will still return a streaming response . """

# convert json to dictionary
response_in_dict = json.loads(re.text)
print(response_in_dict['response']) # actual response text is in key 'response'
  
```

# Now we have two endpoints for making request to ollama , one is `api/generate` and other is `api/chat`
Let's see difference between them and see how each one works :
## ✅ 1. /api/generate (For Single-Prompt Generation)
- Generates a response for a single prompt.
- Does not maintain chat history—each request is independent.
- Suitable for one-time queries or single-response completions.

### Example Usage (Python)
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": "What is AI?", "stream": False}
)

print(response.json())  # Full response
```

### Response Format
```json
{
  "response": "AI stands for Artificial Intelligence...",
  "model": "llama3",
  "done": true
}
```

## ✅ 2. /api/chat (For Multi-Turn Conversations)
- Used for chat-based interactions.
- Can Maintains chat history(if we make that kind of functionality) for context-aware responses.
- Suitable for conversational AI.

### Example Usage (Python)
```python
import requests

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is AI?"}
]

response = requests.post(
    "http://localhost:11434/api/chat",
    json={"model": "llama3", "messages": chat_history, "stream": False}
)

print(response.json())  # Full response
```

### Response Format
```json
{
  "message": {
    "role": "assistant",
    "content": "AI stands for Artificial Intelligence..."
  },
  "model": "llama3",
  "done": true
}
```
- The response includes `role: assistant`, indicating the bot's reply.
- This can be used in a loop to maintain conversation history.

## 🔥 Key Differences:
| Feature             | /api/generate | /api/chat |
|---------------------|--------------|-----------|
| **Single-turn response** | ✅ Yes | ❌ No |
| **Multi-turn chat** | ❌ No | ✅ Yes |
| **Can Maintains history(if we make that kind of functionality)** | ❌ No | ✅ Yes , Chat history maintains on the client side |
| **Use case** | Standalone prompts | Conversational AI |

## 🏆 Which One Should You Use?
- **If you need a single response** → Use **/api/generate**.
- **If you are building a chatbot** → Use **/api/chat**.

***Note : Again , Ollama /api/chat does NOT store chat history internally by itself.
      You must maintain and send chat history in every request that allows full control over the conversation memory.
      If you send only the current message without past history, Ollama will respond without context (just like /api/generate).*** 

[Github docs to explore different endpoints of ollama and to see how each one works , basically what we did using commands in cli can also be done using rest api](https://github.com/ollama/ollama/blob/main/docs/api.md)

- Python and Node.js code for sending the request to llm and get response is available in separate files

## So what we observe is that there are different ways to interact with Ollama and its models :
1. CLI - Command Line Interface (Already saw) 
2. Ui-based Interface (now see)
3. API (Already saw)
4. Ollama Python Library (will see after ui-based interface)
### So now we can also use msty.app for interact with ollama and its models (for accesing through ui)

[See this clip to understand how to use msty.app]
(https://youtu.be/GWB9ApTPTv4?si=5itT4qt1hdN8hA5a&t=4385)
