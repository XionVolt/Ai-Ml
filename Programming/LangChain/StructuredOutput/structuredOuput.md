- [What is Structured Output](https://youtu.be/y5EmRr1O1h4?si=2r_z1xHUkd7Ho5-Y&t=127) 

   - ***In LangChain, structured output refers to the practice of having language models return responses in a well-defined data format (for example, JSON), rather than free-form text. This makes the model output easier to parse and work with programmatically***  

- [Why we need structured Output](https://youtu.be/y5EmRr1O1h4?si=Wcs9R-isaWhGkID5&t=321)

- [Two types of models, those who can by default give structured output and those who not know to give structured output](https://youtu.be/y5EmRr1O1h4?si=8RCZjP5h2fFE7Dyn&t=701)

----
- [***with_structured_output*** function](https://youtu.be/y5EmRr1O1h4?si=7AcGZ8AVv2XpZofN&t=847)
   - [Different ways to specify data format](https://youtu.be/y5EmRr1O1h4?si=-m-EUUuGNzaj-fHO&t=885)
        1. [Type Dictionary](https://youtu.be/y5EmRr1O1h4?si=ZNx8vOKoXX2Gv0fh&t=935)
            - [simple TypedDict](https://youtu.be/y5EmRr1O1h4?si=XOw2GaUAgSl4GNPe&t=1277)
            - [annotated TypedDict](https://youtu.be/y5EmRr1O1h4?si=QSmpEa33p4MoVUG1&t=1607)    

- [Pydantic, Data Validation](https://youtu.be/y5EmRr1O1h4?si=m-7iMm2vmfZze_fI&t=2147)
   - Pydantic is a data validation and data parsing library for Python. It ensures that the data you work with is correct, structured, and type-safe.
   - [How pydantic works? With examples](https://youtu.be/y5EmRr1O1h4?si=JI5TX_RZgdk7ING5&t=2257)
   - [How to set default values using pydantic](https://youtu.be/y5EmRr1O1h4?si=xoPT2t5xVm-zr45u&t=2477) 
   - [How to use Optional feeds of `typing` module in pydantic](https://youtu.be/y5EmRr1O1h4?si=c9fV5E7qQc2crYQI&t=2531)
   - [Coerce done by pydantic](https://youtu.be/y5EmRr1O1h4?si=a6a_mikjFaDlrtV9&t=2631)
   - [BultIn validation in pydantic, example `EmailStr` type provide by it ](https://youtu.be/y5EmRr1O1h4?si=Phik_L-nXLUEG03w&t=2697)
   - [Field Function in pydantic](https://youtu.be/y5EmRr1O1h4?si=aqvMEQOBaD3v41zV&t=2775)
   - [How to extract data from pydantic object](https://youtu.be/y5EmRr1O1h4?si=uMXZzBvyu4EoLvet&t=3337)
----
[Using `json_schema.json` for structured output, use it when your project not using the single language](https://youtu.be/y5EmRr1O1h4?si=dsWr_CqQ2nZfAheI&t=3397)

----

[We see 3 ways to define schema, json_schema.json, TypedDict and pydantic, which to use when?](https://youtu.be/y5EmRr1O1h4?si=1oGtWCpL7MW2oEVj)

-----

[When we call our model `with_structured_output` method we can tell our model, by which method we want structured output, `json_schema` or `function_calling`  ](https://youtu.be/y5EmRr1O1h4?si=JKQAmWFzMUmecdwe&t=3897)

***But there are some models who not support structured output itself, like `Tinyllama`, in that case we have to make output parsers on our own***

-----

[Output Parsers](https://youtu.be/Op6PbJZ5b2Q?si=m4DI7nKCTdZ_6UOD)