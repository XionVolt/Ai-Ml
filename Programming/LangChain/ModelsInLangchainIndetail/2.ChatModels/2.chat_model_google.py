# let's take example, how to use google chat model in langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv() # we get our api key

# load_dotenv()
# --------------------------------------------------------------------------------------------------------

# load_dotenv() is a function from the python-dotenv package that loads environment variables from a .env file into the Python environment (os.environ).
""" # How it works in your code?
1. It looks for a .env file in the current directory (or parent directories if not found).
2. Loads the variables defined in the file into the environment.
3. Allows your code to access these variables using os.getenv(). """

""" 
How does this relate to LangChain?
- LangChain needs an API key to access Google's Gemini API.

- If load_dotenv() is not called, the API key might not be found, causing authentication errors.

- You can then retrieve the key like this:

```
import os
api_key = os.getenv("GOOGLE_API_KEY") # variable of name GOOGLE_API_KEY will load in the variable ``api_key``
# And pass it explicitly:
```

model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
Does load_dotenv() automatically inject the key into LangChain?
No. load_dotenv() only loads the key into the environment, but LangChain needs either:
"""
""" 
1. The key passed explicitly (google_api_key=api_key).
2. The key set in environment variables beforehand (export GOOGLE_API_KEY=... in terminal). """

""" 
But How does LangChain know which environment variable to use for each provider?
LangChain has predefined expected environment variable names for each provider, including OpenAI, Google Gemini, Cohere, etc. These names are hardcoded in LangChain's integrations.

Where are these predefined variable names stored?
LangChain uses a configuration system where it expects certain environment variables to be set for each provider. You can check the official LangChain documentation or source code to find 
these mappings.
"""
# --------------------------------------------------------------------------------------------------------


model = ChatGoogleGenerativeAI(model='gemini-1.5-pro',max_tokens=100)
response = model.invoke("What is LangChain?")


# print(response.content)

# streaming

for chunk in model.stream("What is LangChain?"):
    print(chunk.content, end="", flush=True)