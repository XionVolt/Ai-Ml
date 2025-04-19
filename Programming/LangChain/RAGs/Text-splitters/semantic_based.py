from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

# Load HuggingFace embeddings
embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# SemanticChunker with valid threshold type
text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",  # ✅ FIXED here
    breakpoint_threshold_amount=1
)

# Read input text
with open('someText.txt') as f:
    sample = f.read()

# Create semantic chunks
docs = text_splitter.create_documents([sample])
# print(docs)


for i, doc in enumerate(docs):
    print('\n\n',f'Semantic Chunk {i+1}:','\n')
    print(doc.page_content)
    print('---')