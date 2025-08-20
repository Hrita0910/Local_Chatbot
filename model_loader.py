# model_loader.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def load_model():
    """
    Loads TinyLlama optimized for CPU performance.
    """
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token  # Important for padding
    
    print("Loading model for CPU (this may take a moment)...")
    # CPU-specific optimizations
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float32,  # Use float32 for better CPU compatibility
        device_map="cpu",  # Force CPU usage
        low_cpu_mem_usage=True,  # Optimize memory usage
        offload_state_dict=True,  # Help with memory management
    )
    
    print("Creating pipeline...")
    # CPU-optimized pipeline
    text_generation_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        #device=-1,  # -1 means CPU
        #torch_dtype=torch.float32,
    )
    
    print("TinyLlama loaded successfully on CPU!")
    print("Note: Responses may take 10-30 seconds on CPU...")
    return text_generation_pipeline

if __name__ == "__main__":
    print("Testing CPU model loading...")
    pipe = load_model()
    print("TinyLlama CPU model loaded successfully!")