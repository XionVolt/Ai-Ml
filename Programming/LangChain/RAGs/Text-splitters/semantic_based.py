from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

import os 
from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceInferenceAPIEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text_spltiter = SemanticChunker(
    HuggingFaceInferenceAPIEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
),
breakpoint_threshold_type="standard-deviation", # understand breakpoint_threshold_type -> https://youtu.be/SEWS9P4ODmc?si=PSKOPGCc5g-36BpP&t=3287
breakpoint_threshold_amount=1, # understand breakpoint_threshold_amount -> https://youtu.be/SEWS9P4ODmc?si=Fbk2m1c6kOiDj1t6&t=3337
)