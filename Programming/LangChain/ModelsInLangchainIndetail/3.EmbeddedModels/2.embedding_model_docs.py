from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

import os 
from dotenv import load_dotenv
load_dotenv()

# Your Hugging Face API key
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")


# Initialize the embedding model
embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=api_key,
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# for multiple sentence
documents = ["This is an example sentence.", "This is another example sentence."]
embedding_vector = embeddings.embed_documents(documents)

print(embedding_vector)  # Output: List of floats representing the embedding