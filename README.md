# CPU-Optimized Chatbot

This project provides a simple, terminal-based chatbot powered by the `TinyLlama-1.1B-Chat-v1.0` model. It is specifically designed and optimized to run on a standard **CPU**, making large language models accessible for users without a dedicated GPU. The application includes a conversational memory system to maintain context and is built with memory-saving techniques to ensure it runs smoothly on low-resource machines.

## ✨ Features

* **🖥️ CPU-First Design**: Runs entirely on your computer's CPU, no GPU required
* **🪶 Lightweight Model**: Utilizes the efficient and compact `TinyLlama-1.1B` model
* **🧠 Conversational Memory**: Remembers the last few exchanges (configurable window size) to provide context-aware responses
* **⚡ Memory Optimized**: Employs techniques like `low_cpu_mem_usage` and state dict offloading to minimize RAM usage during model loading
* **🎯 Simple Interface**: A straightforward command-line interface for easy interaction
* **🔄 Context Preservation**: Maintains conversation flow across multiple exchanges

## 🚀 Setup Instructions

Follow these steps to get the chatbot running on your local machine.

### 1. Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher ([Download here](https://www.python.org/downloads/))
- Git ([Download here](https://git-scm.com/downloads))

### 2. Clone the Repository

Open your terminal and clone this repository to your local machine:

```bash
git clone https://github.com/Hrita0910/Local_Chatbot.git
cd Local_Chatbot
```

### 3. Create a Virtual Environment

It is highly recommended to create a virtual environment to manage project dependencies.

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies

Install all the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 🎮 How to Run

1. **Activate your virtual environment** (if not already activated):
   - Windows: `.\venv\Scripts\activate`

2. **Run the chatbot**:
   ```bash
   python interface.py
   ```

3. **Wait for model loading**: The first time you run the script, it will download the TinyLlama model from Hugging Face (approximately 4.4 GB). This will take several minutes and requires an internet connection. Subsequent launches will be faster.

4. **Start chatting**: Once you see the `Chatbot is ready!` message, you can start typing your messages.

5. **Exit**: To end the conversation, type `/exit` and press Enter.

> ⚠️ **Performance Note**: Since this runs on CPU, response generation can take **10 to 30 seconds** depending on your CPU's performance. Please be patient!

## 💬 Sample Interaction

Here's an example of a conversation with the chatbot:

```
User: What is the currency of USA?          
Bot: The currency of the United States is the United States dollar (USD).

User: For India?
Bot: Yes, India uses the Indian rupee (INR) as its currency. The INR is a currency code of the Indian rupee.

User: and China?
Bot: Yes, China uses the yuan (CNY) as its currency. The CNY is a currency code of the yuan.

User: /exit
Exiting chatbot. Goodbye! 👋
```

## 📁 Project Structure

```
project-directory/
├── interface.py
├── chat_memory.py
├── model_loader.py        
├── requirements.txt      
├── README.md            
             
```

## 🚧 Known Limitations

- **Response Time**: CPU inference is significantly slower than GPU (10-30+ seconds per response)
- **Model Size**: Limited to smaller models due to CPU memory constraints
