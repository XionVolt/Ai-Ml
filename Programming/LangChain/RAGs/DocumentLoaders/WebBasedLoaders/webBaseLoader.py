from langchain_community.document_loaders import WebBaseLoader


url = "https://www.amazon.in/HP-i5-1334U-Microsoft365-Office2024-15-6inch/dp/B0DTK9DZB4/ref=sr_1_2_sspa?sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)