from langchain_community.document_loaders import CSVLoader

# Load CSV data

loader = CSVLoader(file_path="languages_perferences.csv",encoding="utf-8")

docs = loader.load()

print(docs)

print(docs[0].page_content) # give columns of first row
print(docs[0].metadata) # give metadata of first row

print(docs[-1].page_content) # give columns of last row