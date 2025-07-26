from llama_cpp import Llama

model_paths = {
    'gemma-3-4B-it-QAT-Q4_0': '/Users/billylokhl/.lmstudio/models/lmstudio-community/gemma-3-4B-it-QAT-GGUF/gemma-3-4B-it-QAT-Q4_0.gguf',
    'DeepSeek-R1-Distill-Qwen-7B-Q4_K_M': '/Users/billylokhl/.lmstudio/models/lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf'
}

# Example Prompt
prompt = "Write a short poem about the ocean."

for model_name, model_path in model_paths.items():
    # Initialize the Llama model
    verbose = False
    try:
        llm = Llama(model_path=model_path, n_ctx=2048, verbose=verbose)  # Adjust n_ctx based on your model and context length
    except Exception as e:
        print(f"Error loading the model: {e}")
        exit()
    
    # Generate Text
    try:
        print(f'\nprompt:\n\n{prompt}\n')    
        output = llm(prompt, max_tokens=50)  # Adjust max_tokens as needed
        print(f'model: {model_name}')
        print(f'generated text: {output["choices"][0]["text"]}')
    except Exception as e:
        print(f"Error generating text: {e}")

