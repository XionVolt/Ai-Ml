# Text splitting on pdf file -> https://youtu.be/SEWS9P4ODmc?si=kHOtRBxPgFJ7yUkZ&t=1007

from langchain.text_splitter import CharacterTextSplitter



with open("someText.txt") as f:
    text = f.read()

# Split text into smaller chunks of 100 characters each
text_splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separator=""
    
    )
result = text_splitter.split_text(text)
print(len(result),result[0])