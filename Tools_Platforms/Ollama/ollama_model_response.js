async function generateResponse() {
    try {
      const response = await fetch("http://127.0.0.1:11434/api/generate", {
        method: "POST",
        
        body: JSON.stringify({
          model: "llama3.2",
          prompt: "Hello, how are you?",
          stream: false, 
        }),
      });
  
      const data = await response.json();
      console.log(data.response); 
    } catch (error) {
      console.error("Error:", error);
    }
  }
  
  generateResponse();
  