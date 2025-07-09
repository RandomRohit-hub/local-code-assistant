
# 🤖 Multi-language Code Assistant

This is a local AI-powered multi-language code assistant built using Python, Gradio, and a local LLM API (such as Ollama). It allows you to interact with AI models for code generation and assistance across various programming languages.

---

## 🚀 Features

- Local language model integration (e.g., LLaMA3 via Ollama)
- Multi-language coding support
- Gradio-based interactive web interface
- Fully offline and privacy-friendly

---

## 🛠 Requirements

Before running the project, make sure the following are installed on your system:

### ✅ System Requirements

- Python 3.8+
- Git
- (Optional) CUDA-enabled GPU for faster inference

### 📦 Python Libraries

Install via `requirements.txt`:
```bash
pip install -r requirements.txt
````

### 🧠 Local LLM (Ollama)

This app uses a local API served by [Ollama](https://ollama.com/) to generate responses from models like `llama3`.

1. Download and install Ollama:

   * [https://ollama.com/download](https://ollama.com/download)

2. Pull the model:

   ```bash
   ollama run llama3
   ```

   This starts a local server at `http://localhost:11434`.

> ℹ️ Make sure this server is running before launching the app.

---

## 💻 How to Run on Any PC

Follow these steps to clone and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/RandomRohit-hub/Multi-language-code-assistant.git
cd Multi-language-code-assistant
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Local LLM Server

Make sure `Ollama` is running in a separate terminal:

```bash
ollama run llama3
```

This will host a server at `http://localhost:11434`.

### 5. Run the App

Now launch the Gradio interface:

```bash
python app.py
```

The app will open in your browser at `http://localhost:7860`.

---

## 🧪 Known Issues

* If Ollama is not running, you will get a `ConnectionRefusedError` at port `11434`.
* The assistant relies on a local endpoint (`/api/generate`) — modify `app.py` if you're using a different LLM or server.

---

## 🧩 Future Improvements

* Add support for multiple LLMs (OpenAI, Gemini, etc.)
* Add syntax highlighting for generated code
* Add voice-to-code or image-to-code functionality

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome!

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

* **Rohit Sharma**
* GitHub: [@RandomRohit-hub](https://github.com/RandomRohit-hub)

```



Would you also like me to:
- Generate a `requirements.txt` from your code?
- Create a `.bat` or `.sh` script to auto-run everything?
Let me know and I’ll do that next.
```
