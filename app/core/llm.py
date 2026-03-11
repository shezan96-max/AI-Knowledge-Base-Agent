import subprocess

def ask_llm(prompt):
    process = subprocess.Popen(
        ['ollama','run','phi3:mini'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="UTF-8"
    )

    output,error = process.communicate(input=prompt)

    return output.strip()
    