import subprocess

OLLAMA_PATH = "/usr/local/bin/ollama"  

def query_local_llm(prompt):
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", "deepseek-coder", prompt],  
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print("⚠️ Fehler bei LLM-Aufruf:")
            print(result.stderr)
        return result.stdout
    except Exception as e:
        print("❌ Ausnahme bei LLM-Abfrage:", e)
        return None
