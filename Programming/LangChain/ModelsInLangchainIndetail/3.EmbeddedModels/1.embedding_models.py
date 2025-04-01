# See this video to see how to work with embedding models - https://youtu.be/HdcLE8JuMrA?si=mTsgChA08n52ARsi&t=4685
# Big the vector more contextual meaning will capture, small the vector less contextual meaning will capture

# -------------------------------------------------------------
# Interact with openai embedding models - https://youtu.be/HdcLE8JuMrA?si=GJajL_MlX2T9dp_r&t=4757, 

# let's see hugginface examples
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

# Test embedding generation
text = "This is an example sentence."
embedding_vector = embeddings.embed_query(text)

print(embedding_vector)  # Output: List of floats representing the embedding
