from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path= r"C:\Users\Vedansh\Documents\Books📚",
    glob= "*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(docs[0])