# Customizing Ollama Model with Modefile

This guide explains how to customize an **Ollama** model using a `Modefile` or any other name. This allows you to configure parameters like temperature, system prompts(**not a parameter**), and other model behaviors.

---

## **1. Creating a `Modefile`**

Create a file named `Modefile` and add the following:

```text
FROM llama3.2

PARAMETER temperature 0.3

SYSTEM """
You are a smart model 
"""
```

### **Explanation:**
- `FROM llama3.2` → Uses `llama3.2` as the base model. You can give any model name here , obviously that should be pulled from ollama hub first.
- `PARAMETER temperature 0.3` → Controls randomness (lower values = more deterministic, higher = more creative).
- `SYSTEM` → Sets a default system prompt that shapes model responses.

---

## **2. Understanding `SYSTEM`**
The `SYSTEM` directive in the `Modefile` defines a system-level instruction for the model. This prompt sets the model's behavior and personality before any user interaction. It ensures that responses align with a specific goal or tone. 

For example:
```text
SYSTEM """
You are an AI designed to assist with coding-related tasks. Respond concisely and provide accurate technical information.
"""
```
- Note: SYSTEM is not a PARAMETER, but it acts as a system instruction that defines the model’s behavior.
- How SYSTEM Works
  - It does not affect Parameters like randomness, length, or token selection directly.
  - It acts like a hidden system prompt that influences responses before user input is considered.
  - It helps create role-based AI models (e.g., "You are a coding assistant" or "You are a legal expert").

This would make the model focus on technical accuracy and brevity.

---

## **3. Building and Running the Custom Model**

### **Build the model:**
```bash
ollama create my-custom-model -f Modefile
```

### **Run the model:**
```bash
ollama run my-custom-model
```
So now our  `my-custom-model`  use those parameters(we defined in `Modefile`) and system prompt.

---

## **4. Additional Useful Parameters**

You can add more `PARAMETER` settings to customize your model further:

### **Response Control**
- `PARAMETER temperature 0.7` → Increases randomness (0.1 = predictable, 1.0 = creative).
- `PARAMETER top_k 50` → Limits responses to the top 50 most probable tokens.
- `PARAMETER top_p 0.9` → Nucleus sampling (higher = more diverse responses).
- `PARAMETER repetition_penalty 1.2` → Reduces repetitive outputs.
   - How It Works:
        - repetition_penalty > 1.0 (e.g., 1.2) → Reduces repetitive words/phrases by penalizing already used tokens.
        - repetition_penalty = 1.0 → No penalty (default behavior).
        - repetition_penalty < 1.0 (e.g., 0.8) → Increases repetitiveness, making the model more likely to reuse words.

### **Performance Optimization**
- `PARAMETER context_length 4096` → Sets context window size (affects memory usage).
- `PARAMETER batch_size 8` → Defines how many tokens are processed in parallel.
- `PARAMETER num_threads 4` → Allocates CPU threads for faster inference.
- `PARAMETER num_ctx 4096` → Sets the maximum number of tokens the model can handle. Means how many tokens the model can handle in one go this is also called as context length.

### **System Behavior**
- `PARAMETER stop "\n\n"` → Stops generation at a specific sequence.
- `PARAMETER presence_penalty 0.5` → Encourages new topic exploration.
- `PARAMETER frequency_penalty 0.5` → Reduces overused phrases.

### **Custom Tokenizer**
A tokenizer is responsible for converting text into smaller units called **tokens**, which the model processes. Using a custom tokenizer allows you to:
- Optimize tokenization for specific languages or domains.
  - Tokenization refers to the process of converting text into smaller parts, known as tokens, in Natural Language Processing (NLP) and machine learning, which helps machines understand human language by breaking it down into more manageable units
- Reduce token count for better efficiency.
- Customize how words and phrases are split.

To use a custom tokenizer, specify it in your `Modefile`:
```text
TOKENIZER my-tokenizer.json
```

This requires a valid `my-tokenizer.json` file, which can be generated using **SentencePiece**, **Byte-Pair Encoding (BPE)**, or other tokenization libraries. Ensure the tokenizer is compatible with the base model to avoid mismatches in tokenization.

---
## **5. Example: Advanced Modefile**
```text
FROM llama3.2

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER repetition_penalty 1.2
PARAMETER context_length 4096
PARAMETER batch_size 8
PARAMETER num_threads 4

SYSTEM """
You are an advanced AI model designed to assist with programming tasks.
Provide well-structured responses and optimize for clarity.
"""
```


---

## **6. Conclusion**
Using a `Modefile`, you can fine-tune how your Ollama model behaves, ensuring it aligns with your needs. Experiment with different parameters to optimize performance and response quality!
