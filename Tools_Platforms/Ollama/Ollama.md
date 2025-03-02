# What is Ollama ?
Ollama is an open source tool that is designed to essentially simplify the process of running LLM locally meaning on your hardware. 
[Resource for learning about Ollama](https://youtu.be/GWB9ApTPTv4?si=t_BxY0x4EAc2cL6v)
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
  - [Quantization](https://youtu.be/GWB9ApTPTv4?si=YrUXLirO6dgbQjeg&t=2367)
  
[Some more Ollama Commands](https://youtu.be/GWB9ApTPTv4?si=jSiB47IfJ8oRa8iN&t=2640)


- [We can also modify or we can say customize our model](https://youtu.be/GWB9ApTPTv4?si=gZ2JxzTaqqTRKC4J&t=3240) because we can add certain pieces of metadata to the model to what we want it to be . 
- Temperature in context of Model : Temperature is what allows the model to be more creative , more direct ..., More detailed explanation is in separate targeted file . 
- Basically we can also set different parameters for our Ml Model in separate file , for customize(fine tune) the model according to our needs
ModelFile explained in detail in separatefile named `modefile-customizeModel.md`


ollama serve at some end point locally , and it all serve at localhost:11434 , that means we can generate the response using rest Api

So we can generate response using rest api 

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
re = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2", "prompt": "Hello, how are you?","stream": False})  """ Ollama supports 
"stream": False" in the JSON payload, 
which makes it return the full response at once. 
 So we have to assign stream flag to False in 
 payload instead of requests.post parameter , because 
in our case, Ollama's /api/generate returns a streaming response by default, so even if you set stream=False in parameter, 
it won't work as ollama will still return a streaming response . """

print(re.text)
  
```

...topic in progress 