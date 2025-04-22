# !pip install langchain chromadb faiss-cpu openai tiktoken langchain_openai langchain-community wikipedia

from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import os
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# from google.colab import userdata # (if you using google colab)
# huggingfacekey =  userdata.get('HUGGINGFACEHUB_API_TOKEN')

huggingfacekey =  getenv('HUGGINGFACEHUB_API_TOKEN')


# ✅ Set your Hugging Face API Key (already done)

# ✅ Initialize embedding function
embedding_function = HuggingFaceInferenceAPIEmbeddings(
    api_key=huggingfacekey,
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ✅ Define documents
docs = [
    Document(page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and passionate leadership.",
            metadata={"team": "Royal Challengers Bangalore"}),

    Document(page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and explosive batting.",
            metadata={"team": "Mumbai Indians"}),

    Document(page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
            metadata={"team": "Chennai Super Kings"}),

    Document(page_content="KL Rahul is a stylish and technically sound batsman, known for his consistency and adaptability in different formats. He has been a key player for Punjab Kings.",
            metadata={"team": "Punjab Kings"}),

    Document(page_content="David Warner, one of the top overseas performers in IPL, has captained Sunrisers Hyderabad to an IPL title. His explosive starts have often set the tone.",
            metadata={"team": "Sunrisers Hyderabad"}),
]


vector_store =  Chroma(
    embedding_function = embedding_function, # so this embedding model is used by chroma db to create embeddings(and then it will store those embeddings)
    persist_directory = "chroma_db", # this is the directory where documents in the form of vectors are stored, mean our chroma db store here
    collection_name = "sample" # this is the name of the collection in the chroma db
)

# store documents in vector store and return list of id of store documents
vector_store.add_documents(docs) # to add documents to vector store


# it gives you embeddings, documents, metadatas of all the documents in the vector store
print(vector_store.get(include=['embeddings','documents','metadatas'])) 


# Perform a similarity search to find the top 2 results based on the query
print(vector_store.similarity_search(query="Who is a calm IPL captain?", k=2)) # output document object 
# k=2 means, top 2 results if its the only 1 result then it will return 1 result 2 times

""" same as above but with score"""


vector_store.similarity_search_with_score(query="Who is a calm IPL captain?", k=2) 

"""Note: With `similarity_search` and `similarity_search_with_score` also have a filter parameter that you can use to filter the results based on metadata."""



# ## Note: 
# **Low score** means high similarity and **high score** means low similarity, 
# this is because most vector databases like Chroma use Euclidean distance 
# or cosine distance as the similarity metric.
# These are distance-based, not similarity scores.

# If you want to invert the logic and see "similarity scores" instead of distances, you can compute it like this:
# `similarity_score = 1 - distance_score


## to update a document
updated_doc1 = Document(page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and passionate leadership. He mostly played from RCB Team in Ipl",
            metadata={"team": "Royal Challengers Bangalore"})


vector_store.update_document(document_id='c3619d66-abf5-4859-92e9-7b3165c289b3', document=updated_doc1)


## to delete a document
vector_store.delete(ids=['24a7ff1c-0a4a-4fec-911a-34453f0ca070'])
