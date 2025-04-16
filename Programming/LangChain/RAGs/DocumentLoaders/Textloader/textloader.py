from langchain_community.document_loaders import TextLoader

loader = TextLoader("blackholes.txt")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)