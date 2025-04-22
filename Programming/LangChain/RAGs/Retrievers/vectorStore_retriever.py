from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

from langchain.vectorstores import Chroma
from langchain.schema import Document
import os
# from google.colab import userdata # (if you using google colab)
from dotenv import load_dotenv
from os import getenv

load_dotenv()


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


# Step 3: Create Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_function,
    collection_name="my_collection"
)

# Create a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
print(retriever)
# Output
"""VectorStoreRetriever(tags=['Chroma', 'HuggingFaceInferenceAPIEmbeddings'], vectorstore=<langchain_community.vectorstores.chroma.Chroma object at 0x79470e6f32d0>, search_kwargs={'k': 2})"""


results = retriever.invoke("Virat kohli")
print(results)

# Output
"""[Document(metadata={'team': 'Chennai Super Kings'}, page_content='MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.'),
 Document(metadata={'team': 'Chennai Super Kings'}, page_content='MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.')]"""