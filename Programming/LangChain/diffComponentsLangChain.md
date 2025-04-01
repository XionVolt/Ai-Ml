[There are 6 different components in langchain](https://youtu.be/-xSJA8-o6Eg?si=egs8arE5UeWWqlaL&t=295)
1. [Models](https://youtu.be/-xSJA8-o6Eg?si=mSNaVhgcYpL7h1t5&t=345)
    - Models are Core Interfaces through which you interact with AI models.  

    - [Example Codes](https://youtu.be/-xSJA8-o6Eg?si=_LsdNn-kocwS-goQ&t=727)

    - [In langchains there are 2 types of models with interact with LLMs, language models and embedding models](https://youtu.be/-xSJA8-o6Eg?si=XM53gLlgEcLNcT71&t=797)  
         - [Different types of language and embedding models available in langchain](https://youtu.be/-xSJA8-o6Eg?si=5VhNdejW4F15vg_g&t=890)

2. [Prompts](https://youtu.be/-xSJA8-o6Eg?si=s_yQ59pPp31H6Umb&t=1010)
    - Allow us to create dynamic, reusable prompts(inputs we provide to llms). 
    - Allow us to do role based prompting and few shot prompting. 
    - [All Examples and Codes](https://youtu.be/-xSJA8-o6Eg?si=QWFA_08FvlbcG6zg&t=1145)
        - [Dynamic and reusable prompts](https://youtu.be/-xSJA8-o6Eg?si=usr1e2Ua6YPRj-j4&t=1197)
        - [Role based prompts](https://youtu.be/-xSJA8-o6Eg?si=SGMGaIXFQBN5w91g&t=1241)
        - [Few shot prompting](https://youtu.be/-xSJA8-o6Eg?si=kIqs_cs6fgI6-rNd&t=1301)

3. [Chains](https://youtu.be/-xSJA8-o6Eg?si=LosZtmBBbJm1P2Cv&t=1460)
   - Helps to build pipelines, one of the good thing about this pipeline, is that output of one component becomes input of another component automatically.
   - [Example](https://youtu.be/-xSJA8-o6Eg?si=ZRiGhUqxL-QUiAen&t=1507)
4. [Indexes](https://youtu.be/-xSJA8-o6Eg?si=xwYgm4UfI-uhpsny&t=1920)
   - Connect your application to external knowledge, such as PDFs,  website or databases.
   - Indexes has 4 things:
      - [Doc loader](https://youtu.be/-xSJA8-o6Eg?si=7t4LNQYhCTRyIAhg&t=2137)
      - [Text splitter](https://youtu.be/-xSJA8-o6Eg?si=QNQj8qwYTFgrx7Yj&t=2167)
      - [Vector store(Database) - Since we are storing vectors in Database](https://youtu.be/-xSJA8-o6Eg?si=pPY6UKEFZzQgwx1k&t=2161)
      - [Retriever](https://youtu.be/-xSJA8-o6Eg?si=ZaZdC6hWuDKED8Hc&t=2251)
5. [Memory](https://youtu.be/-xSJA8-o6Eg?si=pDKROgQgClC7xbEx&t=2351)
    - [LLM API calls are stateless, that's why we have to give our llm each time the history of previois conversations, that can be done in many ways, see this clip](https://youtu.be/-xSJA8-o6Eg?si=BSk0fzxncpi4_d7A&t=2367)
    - [Different types of memory we can use in langchain](https://youtu.be/-xSJA8-o6Eg?si=E1qNQJb_dCGllb69&t=2503)

6. [Agents](https://youtu.be/-xSJA8-o6Eg?si=Vweq36_pnyGK47Ip&t=2647)
   - So basically Ai agents are just evolved form of chatbots with reasoning capabilities and different tools access 
   - With the help of this component we can make Ai Agents
   - [Chain of thought technique for prompting](https://youtu.be/-xSJA8-o6Eg?si=i_gc9X2ed8r3puzR&t=2997)