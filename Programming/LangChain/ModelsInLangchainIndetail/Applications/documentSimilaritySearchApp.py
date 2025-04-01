
# See this video clip to see step by step process by `CampusX`- https://youtu.be/HdcLE8JuMrA?si=aZjFdxe2H8zKJ129&tk=5398

# ----------------------------------------------------------------------
# imports

from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os , re , numpy as np
from dotenv import load_dotenv
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------------------------------------


load_dotenv()

# Your Hugging Face API key
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")


documents = [
    "Artificial intelligence enhances user experience by enabling personalized recommendations, automating repetitive tasks, and improving data-driven decision-making.",
    
    "Machine learning models need large datasets to identify complex patterns, reduce bias, and improve generalization to unseen data.",
    
    "Quantum computing has the potential to break traditional encryption methods while also enabling unbreakable quantum-safe cryptographic techniques.",
    
    "A healthy diet combined with regular exercise boosts metabolism, strengthens the immune system, and reduces the risk of chronic diseases.",
    
    "Advanced AI-powered data analytics tools help businesses extract valuable insights, optimize operations, and make more accurate predictions."
]


# Initialize the embedding model
embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=api_key,
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

questions_embeddings = np.array(embeddings.embed_documents(documents))

# print(np.array(questions_embeddings)[0]) # Output: List of floats representing the embeddings (questions_embeddings)


user_input = input("Enter sentences or words: ")
user_inputs = re.split(pattern=r',(?<!\\)',string=user_input)

embedding_vector = embeddings.embed_documents(user_inputs)


def find_closest_answers(embedding_vector, questions_embeddings):
    return np.argsort(cosine_similarity(embedding_vector, questions_embeddings))[:,::-1]



array_of_most_similar_answers = find_closest_answers(embedding_vector, questions_embeddings).flatten()
print(f'Most similar answers:\n{documents[array_of_most_similar_answers[0]]}\n')

print('Other similar matches:\n')

for index in array_of_most_similar_answers[1:]:
    print(documents[index])