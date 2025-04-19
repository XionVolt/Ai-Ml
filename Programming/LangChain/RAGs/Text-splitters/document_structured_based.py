from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


splitter = RecursiveCharacterTextSplitter.from_language(
    language =Language.MARKDOWN,
    chunk_size=277,
    chunk_overlap=0
)

with open("text-splitters.md", "r") as f:
    text = f.read()

recursive_chunks = splitter.split_text(text)

for chunknumber,chunk in enumerate(recursive_chunks):
    print(f'|------------------------Chunk No: {chunknumber+1}-------------------------|','\n')
    print(chunk,'\n\n')
