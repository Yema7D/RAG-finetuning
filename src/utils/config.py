DOCUMENTS_PATH = "documents/"
LLM_MODEL_FILE_PATH = "src/model-mistral/mistral-7b-instruct-v0.1.Q8_0.gguf"
CONTEXT_SIZE = 8000
MAX_REFERENCES = 4
stop_words = [
    "[Utilisateur]", "[Assistant]", "Utilisateur:", "Assistant:" , "[/INST]", "[/SYS]", "<<SYS>>", "<</SYS>>", "<s>", "</s>", "[SYS]", "[INST]"
]
