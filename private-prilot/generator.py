import json
from llama_cpp import Llama

llm = Llama(model_path="models/codellama-7b-python.Q4_K_M.gguf", n_gpu_layers=1)


def generate(input: str):
    out = llm(input, repeat_penalty=1.1, temperature=0.7, top_p=0.92)
    print(json.dumps(out, indent=2))
    return json.dumps(out)
