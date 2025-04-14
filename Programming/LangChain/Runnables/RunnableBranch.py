from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
parser = StrOutputParser()

generate_report_prompt = PromptTemplate(
    template='Generate a brief report on the following topic\n{topic}',
    input_variables=['topic']
)

generate_summary_prompt = PromptTemplate(
    template='Generate a concise summary of the following report, also mention that you generate summary of the original report because original report was so big\n{report}',
    input_variables=['report']
)

# Step 1: Generate the report
generate_report = RunnableSequence(generate_report_prompt, model, parser)

# Step 2: Create branching logic to decide whether to summarize
def branching_condition(report_text):
    return "summarize"  if len(report_text.split()) > 500 else "pass"

# Step 3: Define the summary generation
generate_summary = RunnableSequence(
    generate_summary_prompt,
    model,
    parser
)

# Step 4: Define the branch
branch_chain = RunnableBranch(
    (lambda x: branching_condition(x) == "summarize", generate_summary),
    RunnablePassthrough() # default takes runnbale, non default cases take tuple of: condition, runnable
)

# Final chain
chain = generate_report | branch_chain

# Invoke with topic input
print(chain.invoke({'topic': 'Black Hole'}))
