from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, load_prompt

from dotenv import load_dotenv
import os
import streamlit as st
import time

# Load environment variables
load_dotenv()

# Model setup
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=250
)

model = ChatHuggingFace(llm=llm)

# UI setup with Streamlit
st.title("AI Research Paper Summarizer")

# List of research papers
research_papers = [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
]

# List of explanation styles
explanation_styles = [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical"
]

# List of explanation lengths
explanation_lengths = [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"
]

# Streamlit UI for user input
selected_paper = st.selectbox("Select Research Paper", research_papers)
selected_style = st.selectbox("Select Explanation Style", explanation_styles)
selected_length = st.selectbox("Select Explanation Length", explanation_lengths)

# Generate dynamic prompt
if st.button("Generate Summary"):

    template = load_prompt('prompt.json')

    # Function to call the model with retries
    def generate_response():
        retries = 3  # Number of retry attempts
        for attempt in range(retries):
            try:
                chain = template | model
                result = chain.invoke({
                    'paper_input': selected_paper,
                    'style_input': selected_style,
                    'length_input': selected_length
                })
                st.success("Here's your summary:")
                st.write(result.content)
                return
            except Exception as e:
                st.error(f"Attempt {attempt + 1} failed: {str(e)}")
                time.sleep(2)  # Wait before retrying

        st.error("Failed to generate a response after multiple attempts. Please try again later.")

    # Generate response
    generate_response()