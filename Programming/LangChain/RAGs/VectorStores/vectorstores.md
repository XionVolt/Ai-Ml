- [why we need vectore stores](https://youtu.be/k13WK0bxQP0?si=wSq_g05w0X6qKOsV&t=67)
    - [know about embeddings and how its used](https://youtu.be/k13WK0bxQP0?si=3x_EXB_5pqdftpky&t=627)
    - [Problems that we might face when making semantic based recommender system(in this example sematic based movie recommender system), and good thing is that, these problems are solved by vector stores](https://youtu.be/k13WK0bxQP0?si=HUcZw8ZUQuCtlyjO&t=887)

- [What are vector stores](https://youtu.be/k13WK0bxQP0?si=KLlr9vC2QcBAuJ4A&t=1107)
  - [understand what can be metadata of vector stores](https://youtu.be/k13WK0bxQP0?si=Aj1ApjyEoz-55WP1&t=1177 )
  - [2 storage options provided by vector stores](https://youtu.be/k13WK0bxQP0?si=gXJAQkGYEM43Ox3Z&t=1227)
  - [understand how indexing enables fast similarity searches, **and centroid vectors of clusters**  way(***one of the way of doing indexing***)](https://youtu.be/k13WK0bxQP0?si=Yd36o5LHhYJoJiga&t=1327)

- [Vector stores vs Vector databases](https://youtu.be/k13WK0bxQP0?si=vDqdEQ6KLxqoGGkh&t=1737)

- [Vector stores in langchain](https://youtu.be/k13WK0bxQP0?si=MATN9gFRGGL3YWhu&t=2027)

- [Understand how to work with vector stores in langchain with `chroma db`(a light weight vector database) example](https://youtu.be/k13WK0bxQP0?si=fccwOs9Nl58MVgnV&t=2227)

- [Hands on code for vector stores in langchain](https://youtu.be/k13WK0bxQP0?si=QivxR-gNGqJaLN8t&t=2387)

Example code:

```py
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import os
from google.colab import userdata # (if you using google colab)


huggingfacekey =  userdata.get('HUGGINGFACEHUB_API_TOKEN')

# ✅ Set your Hugging Face API Key (already done)
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_your_key_here"

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
    persist_directory = "chroma_db",
    collection_name = "sample"

)

vector_store.add_documents(docs) # to add documents to vector store


print(vector_store.get(include=['embeddings','documents','metadatas']))


print(vector_store.similarity_search("Who is a calm IPL captain?", k=2)) # output document object 
# k=2 means, top 2 results if its the only 1 result then it will return 1 result 2 times

```

