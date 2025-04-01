import streamlit as st
import time, os
import json
from huggingface_hub import InferenceClient

# Hugging Face API Setup
API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"

# Initialize the API client
llm_client = InferenceClient(model=MODEL_ID, token=API_TOKEN, timeout=120)

# Streamlit UI setup
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
prompt = f"""
Please summarize the research paper titled "{selected_paper}" with the following specifications:
Explanation Style: {selected_style}
Explanation Length: {selected_length}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""

# Function to call the model with retries
def call_llm(inference_client: InferenceClient, prompt: str):
    retries = 3  # Number of retry attempts
    for attempt in range(retries):
        try:
            with st.spinner("Generating response..."):
                response = inference_client.post(
                    json={
                        "inputs": prompt,
                        "parameters": {"max_new_tokens": 500, "temperature": 0.7}
                    }
                )
                response_json = json.loads(response)  # Convert string response to JSON
                
                # Check if response is a list and extract the first element if needed
                if isinstance(response_json, list):
                    response_text = response_json[0]["generated_text"]  # Adjust indexing based on actual response structure
                else:
                    response_text = response_json.get("generated_text", "No response received.")

                st.write(response_text)  # Display the summary
                return response_text
        except Exception as e:
            st.error(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(2)  # Wait before retrying

    st.error("Failed to generate a response after multiple attempts. Please try again later.") #  that yellow box message


# Handle submission
if st.button("Summarize"):
    call_llm(llm_client, prompt)
