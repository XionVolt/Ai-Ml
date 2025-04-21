[Retrievers in LangChain](https://youtu.be/pJdMxwXBsk0?si=wDjsyLn6A4H34wnU&t=67)

**A retriever is a component in LangChain that fetches relevant documents from a data source(vector stores/databases, APIs, etc.,) in response to a user’s query.**

- There are multiple types of retrievers

- All retrievers in LangChain are runnables

[Types of Retrievers](https://youtu.be/pJdMxwXBsk0?si=oOvEyEfBFwBLwAIj&t=327)

- Based on Data Source
  - [Wikipedia Retriever](https://youtu.be/pJdMxwXBsk0?si=vrhBQFSohKKW1vDw&t=607)
    - [How its different from wikipedia document loader](https://youtu.be/pJdMxwXBsk0?si=C_xuxnb183lE2_3N&t=887)
    - Example Code
      ```py
      from langchain_community.retrievers import WikipediaRetriever
      query = "what is model context protocol?"

      # Initialize the retriever (optional: set language and top_k)
      retriever = WikipediaRetriever(top_k_results=2, lang="en")
      docs = retriever.invoke(query)
      print(docs) 
      # Print retrieved content
      for i, doc in enumerate(docs):
        print(f"\n--- Result {i+1} ---")
        print(f"Content:\n{doc.page_content}...") 
      ```

  - [Vector store retriever](https://youtu.be/pJdMxwXBsk0?si=Th43NeX0xKZ-CpK0&t=947)
