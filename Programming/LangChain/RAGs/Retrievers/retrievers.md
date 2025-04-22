[Retrievers in LangChain](https://youtu.be/pJdMxwXBsk0?si=wDjsyLn6A4H34wnU&t=67)

**A retriever is a component in LangChain that fetches relevant documents from a data source(vector stores/databases, APIs, etc.,) in response to a user’s query.**

- There are multiple types of retrievers

- All retrievers in LangChain are runnables

[Types of Retrievers](https://youtu.be/pJdMxwXBsk0?si=oOvEyEfBFwBLwAIj&t=327)

- Based on Data Source
  - [Wikipedia Retriever](https://youtu.be/pJdMxwXBsk0?si=vrhBQFSohKKW1vDw&t=607)
    - [How its different from wikipedia document loader](https://youtu.be/pJdMxwXBsk0?si=C_xuxnb183lE2_3N&t=887)
  

  - [Vector store retriever](https://youtu.be/pJdMxwXBsk0?si=Th43NeX0xKZ-CpK0&t=947)
  - [Vector store retriever in code](https://youtu.be/pJdMxwXBsk0?si=FWWrIMs8bXrO49ab&t=1037)
  - [What's the point of `vectorstore.as_retriever(search_kwargs={"k": 2})` if `vector_store.similarity_search(query, k=2)` also does the same thing](https://youtu.be/pJdMxwXBsk0?si=zWlMK_C6CwoaCB9P&t=1167)

  
- Based on the retrieval strategy they use
  - [Maximal Marginal Relevance(MMR)](https://youtu.be/pJdMxwXBsk0?si=r0ty-HRrbhSvgkGu&t=1337)
  - [MMR In code](https://youtu.be/pJdMxwXBsk0?si=WUbrAim9lzprTMtS&t=1627)

  - [Multi query retriever](https://youtu.be/pJdMxwXBsk0?si=Dgk0Mg0_MQ1rJbpk&t=1837)
    - [Multi query retriever in code](https://youtu.be/pJdMxwXBsk0?si=4tKSKbC-HMVQjyuc&t=2117)