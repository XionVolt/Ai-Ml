[See this](https://youtu.be/3TGqlQxpuU0?si=ck5kNlalv5nl-c4U&t=27)

# so prompts are basically the input instructions or queries given to a model to guide its output

- [See this video](https://youtu.be/HdcLE8JuMrA?si=NkW65685x2JMFJtz&t=3207)

- [See this video to see about static vs dynamic prompts](https://youtu.be/3TGqlQxpuU0?si=nrppqK1SyEH0Uv2Z&t=637)

- [why use ***PromptTemplate*** over f-strings](https://youtu.be/3TGqlQxpuU0?si=9rxjfp_LWZWq2Ox3&t=1637)

    - [when use PromptTemplate classes that provide by langchain we can also use this shortcut](https://youtu.be/3TGqlQxpuU0?si=f-4hvf32aCWzFGN6&t=2037)

- [different types of meassages in langchain](https://youtu.be/3TGqlQxpuU0?si=qiYNweHgvvSWxDj9&t=2871)

- [summary of what we see until now about langchain about prompts, and about](https://youtu.be/3TGqlQxpuU0?si=wdrVEQbc41u-JiuS&t=3397)

- [***ChatPromptTemplate*** in langchain, for make dynamic prompts for list of messages](https://youtu.be/3TGqlQxpuU0?si=rP-Iq6AGW1ibvF5w&t=3565)
```py
# Example code of how to use ChatPromptTemplate, for build up chat history
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    messages=[
        ('system', 'You are a helpful {role}.'),
        ('human', 'My name is {name}.'),
        ('assistant', 'Hi {name}, how can I help you?'),
    ],
    input_variables=["name", "role"],
)

chat_history = [

    chat_template.format_prompt(name="tira", role="assistant").to_messages(),
    chat_template.format_prompt(name="mimico", role="singer").to_messages(),
    """
    or like this:
    chat_template.invoke({'name':"tira", 'role':"assistant"}).to_messages(),
    chat_template.invoke({'name':"mimico", 'role':"singer"}).to_messages()"""
]

# Print the entire chat history
for i, chat in enumerate(chat_history):
    print(f"\n--- Chat #{i+1} ---")
    for msg in chat:
      if msg.__class__.__name__ == "SystemMessage":
        continue
      print(f"{msg.__class__.__name__}: {msg.content}")

    print(f"--- End of Chat #{i+1} ---")


"""
Output:

--- Chat #1 ---
HumanMessage: My name is tira.
AIMessage: Hi tira, how can I help you?                                                                                                                                                                     
--- End of Chat #1 ---                                                                                                                                                                                      

--- Chat #2 ---
HumanMessage: My name is mimico.
AIMessage: Hi mimico, how can I help you?
--- End of Chat #2 ---
"""
```
[Message Placeholder](https://youtu.be/3TGqlQxpuU0?si=up4Z1aZB5ZSfAHsz&t=4007)