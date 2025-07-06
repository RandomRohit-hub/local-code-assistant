import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"  # Fixed 'localhodt' typo

# ✅ CORRECT dictionary for headers
headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "Owl",
        "prompt": final_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "[No 'response' field found in API response]")
        else:
            return f"❌ Error: {response.status_code}\nDetails: {response.text}"

    except Exception as e:
        return f"⚠️ Request failed: {str(e)}"

# Gradio UI
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt..."),
    outputs="text"
)

interface.launch()
