- [Runnables in langchain](https://youtu.be/u3b-W1NgYa4?si=nxqwu7OOWJQAXkiX)
- [Why runnables exist in langchain](https://youtu.be/u3b-W1NgYa4?si=BSnglrAGjOdgEBIh&t=197)
- [2 code Examples of Making llm based application, using different components](https://youtu.be/u3b-W1NgYa4?si=neN8uen9TuEEugPl&t=643)
    - [Simple llm based app](https://youtu.be/u3b-W1NgYa4?si=8E3KP7DwoerOYFr9&t=707)
    - [pdf-reader app](https://youtu.be/u3b-W1NgYa4?si=w3OIgw2xWKzdAUrG&t=787)
- [Chains Exactly Meaning based on their use, and understand where they are provding ease](https://youtu.be/u3b-W1NgYa4?si=GKIXh_RAB-GUZxFq&t=947)
     - [`LLMChain` function, simplest chain](https://youtu.be/u3b-W1NgYa4?si=5uI67SMDEic73VDb&t=1117)
     - [`RetrieverQAChain`, you can build same application as `pdfreader` in less code and complexity](https://youtu.be/u3b-W1NgYa4?si=b4CjXUNCxWo06VXc&t=1187)

[Different types of chains Examples](https://youtu.be/u3b-W1NgYa4?si=2O47Yj8MvuGF51Sv&t=1437)
   - [***SimpleSequentialChain*** explain](https://youtu.be/u3b-W1NgYa4?si=h-H_ehq5_gLo5Twm&t=1481)

[What problem triggers langchain cause to make runnables](https://youtu.be/u3b-W1NgYa4?si=RmvTaEZHksTntWsP&t=1577)

----

[What are Runnables](https://youtu.be/u3b-W1NgYa4?si=eGscY6r8uGS4VsGr&t=2037)

----

[Imagining like why and how langchain implemented runnables](https://youtu.be/u3b-W1NgYa4?si=qA2_R1QbYtufQbJg&t=2387)

> To be concise, a **runnable is a class that every component inherits from**, it helps to make those components standardized(***must implement some methods within their classes***), so now all components can be connected together using runnables(input of previous component becomes output of next component), which allows us to create big complex workflows with ease.

----

- [Types of Runnables](https://youtu.be/47nc0n-e4_w?si=uEsgPbjAjZiWUlk5&t=277)
    - [Task specific runnables](https://youtu.be/47nc0n-e4_w?si=bfUfkJN-wbgumT2D&t=287)
    - [Runnable Primitives](https://youtu.be/47nc0n-e4_w?si=5Ee0oAsQtg5NXcJT&t=377)

1. [Runnable Sequence](https://youtu.be/47nc0n-e4_w?si=Fl3A5y84HSvjTEWS&t=577) 
    - [Example of Runnable Sequence](https://youtu.be/47nc0n-e4_w?si=bW1oK2gU8yFhO_En&t=667)

2. [Runnable Parallel](https://youtu.be/47nc0n-e4_w?si=w6Md9-Ob5rA6mWZf&t=901)
     - [Example of `RunnableParallel`](https://youtu.be/47nc0n-e4_w?si=rx4reA-RDtayG2v2&t=1035)

3. [Runnable Passthrough](https://youtu.be/47nc0n-e4_w?si=MZl73_G8uyjSGumm&t=1317)
    - [Example of `Runnable Passthrough` returns output as it is you input](https://youtu.be/47nc0n-e4_w?si=wWCDfaZ-T0ER_hql&t=1575)
    - [Real world example of `Runnable Passthrough`](https://youtu.be/47nc0n-e4_w?si=xYhxcRJENSTF3-Up&t=1647)

4. [Runnablelambda](https://youtu.be/47nc0n-e4_w?si=ScQ41B0uLiDgDjbj&t=1807)
    - [Example of `Runnablelambda`](https://youtu.be/47nc0n-e4_w?si=-KYb0y1AA5IWCbeB&t=2077)

5. [RunnableBranch](https://youtu.be/47nc0n-e4_w?si=MOz0DdyO6NoF9O9t&t=2397)