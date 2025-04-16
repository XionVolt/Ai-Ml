from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path= r"C:\Users\Vedansh\Documents\Books📚",
    glob= "*.pdf", # see all patterns, https://youtu.be/bL92ALSZ2Cg?si=NDWNuqTUa8dWsbWt&t=1937
    loader_cls=PyPDFLoader
)

# docs = loader.load()
# print(docs[0])  
# Output like
# Document(page_content='...', metadata={'source': 'path/to/file.pdf'}) , of first page of PDF file in the directory.

# print(docs[0].page_content)
# print(docs[0].metadata)


# lazy loading for very large directories, we will get a generator instead of a list of document objects
lazy_docs = loader.lazy_load()

print(next(lazy_docs))  # prints the first page of the first PDF file in the directory.
print('\n','--------------------------------------------------------------------','\n')
print(next(lazy_docs).metadata) # prints the metadata of the second page of the first PDF file in the directory.
print('\n','--------------------------------------------------------------------','\n')