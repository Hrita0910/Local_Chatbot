# interface.py
from model_loader import load_model
from chat_memory import ChatMemory

def main():
    # Initialize the chatbot components
    print("Loading TinyLlama for GPU. This will be fast! 🚀")
    pipe = load_model()
    memory = ChatMemory(window_size=3)
    print("\n💬 Chatbot is ready! Type '/exit' to end the conversation.")
    print("   Responses will be instant on GPU!\n")
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("User: ").strip()
            
            # Check for exit command
            if user_input.lower() == "/exit":
                print("Exiting chatbot. Goodbye! 👋")
                break
            
            # Prepare the prompt
            conversation_context = memory.get_formatted_history()
            prompt = f"{conversation_context}<|user|>\n{user_input}</s>\n<|assistant|>\n"
            
            # Generate response with GPU
            outputs = pipe(
                prompt,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                pad_token_id=pipe.tokenizer.eos_token_id,
            )
            
            # Extract the response
            bot_response = outputs[0]['generated_text']
            bot_response = bot_response.split("<|assistant|>\n")[-1].split("</s>")[0].strip()
            
            # Print response and add to memory
            print(f"Bot: {bot_response}\n")
            memory.add_exchange(user_input, bot_response)
            
        except KeyboardInterrupt:
            print("\n\nExiting chatbot. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Clearing memory and continuing...")
            memory.clear_history()

if __name__ == "__main__":
    main()