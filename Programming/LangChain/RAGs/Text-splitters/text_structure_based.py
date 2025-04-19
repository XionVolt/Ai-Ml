from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=100,
    length_function=len
)


with open("someText.txt", "r") as f:
    text = f.read()

# Split the text into chunks
chunks = text_splitter.split_text(text)

print("Number of chunks:", len(chunks))
print(chunks)
