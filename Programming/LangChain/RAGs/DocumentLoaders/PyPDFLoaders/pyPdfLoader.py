from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")

# docs = loader.load()
docs = loader.lazy_load() # now loading the entire file into memory, useful for large files, returns a generator basically


print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)