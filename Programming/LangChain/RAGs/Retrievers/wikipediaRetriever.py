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