import os

os.environ['HF_HOME'] = 'E:\Projects\hf_models'
os.environ['TRANSFORMERS_CACHE'] = 'E:\Projects\hf_cache'

# Import the necessary libraries
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# Define custom quantization configuration for BitsAndBytes (BNB) quantization
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                    # Load the model with 4-bit quantization
    bnb_4bit_use_double_quant=True,       # Use double quantization for 4-bit weights
    bnb_4bit_quant_type="nf4",           # Use nf4 quantization method
    bnb_4bit_compute_dtype=torch.bfloat16 # Compute with 4-bit quantized weights in bfloat16 data type
)

# Specify the pre-trained model identifier
model_id = "mistralai/Mistral-7B-v0.1"

# Load the pre-trained model with the specified quantization configuration
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map="auto")

# Load the tokenizer for the same pre-trained model and add an end-of-sequence token
tokenizer = AutoTokenizer.from_pretrained(model_id, add_eos_token=True)