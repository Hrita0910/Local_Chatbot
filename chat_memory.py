# chat_memory.py
class ChatMemory:
    def __init__(self, window_size=3):  
        """
        Initializes the chat memory with a smaller window size for CPU.
        """
        self.window_size = window_size
        self.history = []

    def add_exchange(self, user_input, bot_response):
        """
        Adds a new exchange and applies strict memory management.
        """
        # Clean up responses to save memory (remove extra spaces)
        clean_input = user_input.strip()
        clean_response = bot_response.strip()
        
        self.history.append({"user": clean_input, "bot": clean_response})
        
        # Apply sliding window
        if len(self.history) > self.window_size:
            self.history.pop(0)  # Remove the oldest exchange

    def get_formatted_history(self):
        """
        Formats the conversation history for TinyLlama with CPU efficiency.
        """
        formatted_history = ""
        for exchange in self.history:
            # Use the model's preferred format
            formatted_history += f"<|user|>\n{exchange['user']}</s>\n"
            formatted_history += f"<|assistant|>\n{exchange['bot']}</s>\n"
        return formatted_history

    def clear_history(self):
        """Clears the conversation history to free memory."""
        self.history = []

# For testing
if __name__ == "__main__":
    memory = ChatMemory(window_size=2)
    memory.add_exchange("Hello!", "Hi there! How can I help?")
    print("Current history:\n", memory.get_formatted_history())