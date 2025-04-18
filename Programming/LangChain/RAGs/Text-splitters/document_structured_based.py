from langchain_text_splitter import RecursiveCharacterTextSplitter,Language


splitter = RecursiveCharacterTextSplitter.from_language(
    language =Language.MARKDOWN,
    chunk_size=277,
    chunk_overlap=0
)

with open("someText.md", "r") as f:
    text = f.read()
print(text)
