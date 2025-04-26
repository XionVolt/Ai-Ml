- [What is RAG?](https://youtu.be/bL92ALSZ2Cg?si=dwu74W8QrEZsQ6Et&t=237)
RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.

So basically RAG is a way to make language model smarter by giving it extra information(relevant to that query, that model will use to solve or you can say to find a answer to the query) at the time user ask a question. 


## Benefits of using RAG
1. Use of up-to-date information
2. Better privacy
3. No limit of document size


- [What are the important components of RAG?](https://youtu.be/bL92ALSZ2Cg?si=H6rO_9utRkaTm5UO&t=507)


- [What is RAG | How does RAG Work | RAG Explained](https://youtu.be/X0btK9X0Xnk?si=6USg37W_P9tY1A4e&t=87)
     - [Why Rag](https://youtu.be/X0btK9X0Xnk?si=YfyRsnbNkvg7U1kV&t=221)
     - [Where LLMs might not work good](https://youtu.be/X0btK9X0Xnk?si=4kW2dD8hao2b8aKj&t=507)
     - [Now how to solve these problems, yes its **fine-tuning**, see how](https://youtu.be/X0btK9X0Xnk?si=7NnmyHVBYUIFjqh2&t=637)
     - [Various ways of fine-tuning](https://youtu.be/X0btK9X0Xnk?si=wRSQxruZQCtSBcbr&t=837)
       - [Supervised fine-tuning](https://youtu.be/X0btK9X0Xnk?si=Gf3EVWv3KnXw54T-&t=837) 
          - [Supervised fine-tuning process](https://youtu.be/X0btK9X0Xnk?si=tgwMWeO-fgRKKhh1&t=897)
        - [Continue pretraining](https://youtu.be/X0btK9X0Xnk?si=tgwMWeO-fgRKKhh1&t=897)
    - [Problem with these ways, and their solution is `In context learning`, see how(`few shot` prompting also explained)](https://youtu.be/X0btK9X0Xnk?si=j7XIcPKSLElSHhpn&t=1247)

    - So basically in ***few shot prompting*** **we give few examples of the task we want to perform**(like those examples include input and output) **and then we give the input of the new task we want to perform**(the new task should be related to the examples), and the model will try to predict the output based on the examples we provided. This is a very powerful technique because it allows us to leverage the knowledge that the model has learned from the examples to perform new tasks without having to retrain the model or fine-tune it on a specific dataset. 

    - [`In context learning` is a `emergent property` of llms, but  what is `emergent property` ](https://youtu.be/X0btK9X0Xnk?si=hzbAPIV3tt9M049Q&t=1627)

    ***"An emergent property is a behaviour or ability that suddenly appears in a system when it reaches a certain scale or complexity—even though it was not explicitly programmed or expected from the individual components."***

     - [***Language Models are few shot learners*** Paper](https://youtu.be/X0btK9X0Xnk?si=Q6OyvvLB9WrtHz8E&t=1697)
     - [Why stop here, we can improve it more by improving the, `in context learning`, **all dots like connecting here of like what is the inspiration behind sending user query with relevalnt documents related to that query to the model**](https://youtu.be/X0btK9X0Xnk?si=Tvv64r0G_iTdWx5f&t=1897)

-----

- [Understanding RAG again](https://youtu.be/X0btK9X0Xnk?si=B_DFgOV7cRgrrCre&t=2207)

- [Making Rag requires a 4 steps, understand this 4 steps](https://youtu.be/X0btK9X0Xnk?si=-q27cQzEh3-rIfn-&t=2257)


- 4 steps in summary
1. [Indexing in summary](https://youtu.be/X0btK9X0Xnk?si=wzHg-Q-QDwDd5u9m&t=2277)
2. [Retrieval in summary](https://youtu.be/X0btK9X0Xnk?si=19kKXsV8t1tt9mvL)
3. [Augmentation in summary](https://youtu.be/X0btK9X0Xnk?si=pL14OLdreqLzvV7Y&t=2407)
4. [Generation in summary](https://youtu.be/X0btK9X0Xnk?si=JOaF4asQfAHqqfUL&t=2437)

- 4 steps in detail
1. [Indexing in detail](https://youtu.be/X0btK9X0Xnk?si=Xpz_83_jpXtNZo1t&t=2467)
    - Indexing itself includes 4 steps in it
      - [Document Ingestion](https://youtu.be/X0btK9X0Xnk?si=iof4vL8p69yQ8FB_&t=2507)
      - [Text chunking](https://youtu.be/X0btK9X0Xnk?si=sJhXUflArBbBStKY&t=2587)
      - [Embedding Generation](https://youtu.be/X0btK9X0Xnk?si=1ZiRAkfHRbzhWO51&t=2757)
      - [Storage in vector store](https://youtu.be/X0btK9X0Xnk?si=flsYCoxKp4qQpDV-&t=2857)
2. [Retrieval in detail](https://youtu.be/X0btK9X0Xnk?si=GfTlhxBWJBGFjQLc&t=2937)
3. [Augmentation in detail](https://youtu.be/X0btK9X0Xnk?si=Lxg4-f2PogUD66mo&t=3177)
4. [Generation](https://youtu.be/X0btK9X0Xnk?si=TKi0cHzUD2OwtgPy&t=3247)

----
[Why RAG Better than fine-tuning](https://youtu.be/X0btK9X0Xnk?si=OS76mssdfLEJsBaw&t=3407)

----
## Building RAG

- [Step1: The problem statement](https://youtu.be/J5_-l7WIO_w?si=3vOFsZgxEgHjTxiV&t=57)

- [Step2: Plan of Action](https://youtu.be/J5_-l7WIO_w?si=eaJTGO-nYrvR9Wqb&t=287)

- [Step3: ]()