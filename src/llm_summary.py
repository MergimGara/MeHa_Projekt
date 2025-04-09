import subprocess

def query_local_llm(prompt):
    """
    Lokaler GPT-Aufruf via Ollama + DeepSeek.
    Ruft das Modell `deepseek-coder` über subprocess auf.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "deepseek-coder", prompt],
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