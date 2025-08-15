

#  AI Voice Agent

An interactive **AI-powered voice agent** that converts user speech to text, processes it with a language model, and responds with natural-sounding speech.  
Built with **FastAPI**, this project integrates third-party APIs for **speech-to-text**, **text-to-speech**, and **language model processing**.

---

#  Features

- **Speech Recognition** – Transcribes spoken audio to text using **AssemblyAI**.
- **Intelligent Responses** – Generates context-aware replies using **Google Gemini**.
- **Natural Voice Output** – Converts AI responses to audio with **Murf API**.
- **Chat with History** – Maintains session-based chat history for conversational context.
- **FastAPI Backend** – Provides efficient, asynchronous API endpoints for real-time interaction.
- **Interactive Frontend** – Simple HTML/CSS/JavaScript interface for recording and playing audio responses.

---

#  Tech Stack

**Frontend**  
- HTML, CSS, JavaScript (Web Audio API, Fetch API)

**Backend**  
- Python (**FastAPI**)

**APIs**  
- [AssemblyAI](https://www.assemblyai.com/) – Speech-to-text  
- [Murf](https://murf.ai/) – Text-to-speech  
- [Google Gemini](https://ai.google/) – Natural language processing

**Others**  
- Pydantic – Data validation  
- python-dotenv – Environment variables  
- Python logging – Log management  

---

#  Project Structure

```

ai-voice-agent/
├── services/                     # Third-party service logic
│   ├── stt\_service.py           # AssemblyAI speech-to-text logic
│   ├── tts\_service.py           # Murf text-to-speech logic
│   ├── llm\_service.py           # Google Gemini LLM logic
├── schemas/                      # Pydantic models
│   ├── models.py                 # Request & response schemas
├── static/                       # Frontend files
│   ├── index.html
│   ├── style.css
├── uploads/                     # Temporary uploaded audio files
├── .env                         # Environment variables
├── main.py                      # FastAPI backend
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md

````

---

#  How to Run

###  Clone the Repository
```bash
git clone https://github.com/chaitravc/AI-VOICE-AGENT.git
cd AI-VOICE-AGENT
````

###  Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the project root and add:

```env
ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
MURF_API_KEY=your_murf_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API keys from:

* [AssemblyAI](https://www.assemblyai.com/)
* [Murf](https://murf.ai/)
* [Google Gemini](https://ai.google/)

### Run the Backend Server

```bash
uvicorn main:app --reload
```

Server will run at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### Open the Frontend

Go to:

```
http://127.0.0.1:8000
```

This serves `static/index.html`.

---

## How It Works

1. **Record Audio** – Click the mic button to record.
2. **Transcribe** – Audio is sent to `/api/agent/chat/{session_id}` and transcribed by **AssemblyAI**.
3. **Process** – Text is processed by **Google Gemini** with session-based context.
4. **Generate Audio** – Response converted to speech using **Murf API**.
5. **Play Response** – Audio + text displayed in the browser.

---

#  API Endpoints

| Method | Endpoint                       | Description                             |
| ------ | ------------------------------ | --------------------------------------- |
| POST   | `/api/text-to-speech`          | Convert text to speech using Murf       |
| POST   | `/api/upload-audio/`           | Upload an audio file & return metadata  |
| POST   | `/api/transcribe/file`         | Transcribe audio using AssemblyAI       |
| POST   | `/api/tts/echo`                | Transcribe audio and return it as audio |
| POST   | `/api/llm/query`               | Query Gemini & return text/audio        |
| POST   | `/api/agent/chat/{session_id}` | Chat with history, return text/audio    |
| GET    | `/api/health`                  | Check server status                     |

---

# Dependencies

```txt
fastapi==0.115.0
uvicorn==0.30.6
pydantic==2.9.2
assemblyai==0.33.0
google-generativeai==0.8.3
python-dotenv==1.0.1
murf-ai==0.1.0
```





#  Testing the Voice Agent

1. Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.
2. Click 🎤, speak, and wait for AI to respond.
3. Verify transcription, AI response, and audio playback.
4. Ensure API keys are valid to avoid errors.

---

# Notes

* **Temporary Files** – Stored in `uploads/` and deleted after processing.
* **Logging** – Uses Python’s logging module.
* **Chat History** – Stored in-memory (use a DB like SQLite/Redis for production).
* **Scalability** – Add rate limiting & persistent storage for production.

---



https://github.com/user-attachments/assets/f7a17a08-67e0-409c-a735-93f3323fd1da



```
