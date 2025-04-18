from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://www.flipkart.com/samsung-odyssey-g9-124-46-cm-49-inch-curved-dqhd-led-backlit-va-panel-1000r-curvature-vesa-displayhdr-600-hdr10-height-adjustable-stand-gaming-monitor-ls49fg910ewxxl/p/itm18d77c43040d5?pid=MONHAEETPZSPE3GU&lid=LSTMONHAEETPZSPE3GU2R3AHO&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_2&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=en_v9i5a46WoTDo7DKD_jOXTR2KJRgJxlTsoBs-gj4Qe3d5N8zwK1NDj-tM6TbETXrOauj7__t9lnXHpuduSdrK2fUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=328b140u000000001744865394129"
loader = WebBaseLoader(url)


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = StrOutputParser()

template = PromptTemplate(
    template="You are an AI assistant. You will be given a document. Answer the following question. Question:\n {question} from follwing document:\n {document}",
    input_variables=["document", "question" ]
)

response =  template  | model | parser 

print(response.invoke({"document": loader.load()[0].page_content, "question": "Should i take this monitor as Software and Ai/Ml dev?"  }))