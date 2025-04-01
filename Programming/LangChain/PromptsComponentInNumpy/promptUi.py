from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

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
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

# UI setup
st.header("AI Research Paper Summarizer")

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

# Dropdowns for user input
selected_paper = st.selectbox("Select Research Paper Name", research_papers)
selected_style = st.selectbox("Select Explanation Style", explanation_styles)
selected_length = st.selectbox("Select Explanation Length", explanation_lengths)

# Generate dynamic prompt
prompt = f"Summarize the research paper '{selected_paper}' in a {selected_length} format with a {selected_style} approach."

# we will use prompt template

template = PromptTemplate(
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length
    """,
    input_variables = ['paper_input', 'style_input', 'length_input']

) 

prompt = template.invoke (
    {
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    }
) #! from here we have to complete


# Function to call the model with retries
def generate_response():
    retries = 3  # Number of retry attempts
    for attempt in range(retries):
        try:
            with st.spinner("Generating response..."):
                response = ""
                for chunk in model.stream(prompt):
                    response += chunk.content + " "
                    st.write(chunk.content)  # Streaming output

                return response  # Return the full response
        except Exception as e:
            st.error(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(2)  # Wait before retrying

    st.error("Failed to generate a response after multiple attempts. Please try again later.")

# Handle submission
if st.button("Summarize"):
    generate_response()