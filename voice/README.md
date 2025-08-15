

# AI Voice Agent

An interactive AI-powered voice agent that listens to user speech, processes it using advanced AI models, and responds with natural-sounding speech.

This project integrates:

* **Murf API** – Text-to-Speech conversion
* **AssemblyAI API** – Speech-to-Text transcription
* **Google Gemini API** – Natural Language Understanding & Response Generation

---

##  Features

*  **Speech Recognition**: Converts your spoken words into text using AssemblyAI
*  **Intelligent Response**: Processes text using Google Gemini for accurate, context-aware replies
*  **Natural Voice Output**: Converts AI responses to speech with Murf API
*  **FastAPI Backend**: Efficient API endpoints for real-time interaction
*  **Interactive Frontend**: Simple HTML/CSS/JS interface for recording and playing responses

---

##  Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (FastAPI)
* **APIs**:

  * [Murf API](https://murf.ai) – Text-to-Speech
  * [AssemblyAI](https://www.assemblyai.com) – Speech-to-Text
  * [Google Gemini](https://ai.google) – LLM for text processing
* **Others**: Fetch API for frontend-backend communication


---

##  Project Structure

```
voice/
│── .venv/                       # Virtual environment 
│── audio_outputs/               # Stores generated AI voice audio files
│── static/                      # Frontend static files
│   ├── index.html               # Main user interface
│   ├── index.js                 # Handles frontend logic & API calls
│   ├── style.css                # UI styling
│   └── WhatsApp Image ....jpeg  # Screenshot/image assets
│── uploads/                     # Stores uploaded audio files from user
│── .env                         # Environment variables (API keys, config)
│── main.py                      # FastAPI backend
│── README.md                    # Project documentation
│── requirements.txt             # Python dependencies
```




---



##  How to Run the AI Voice Agent

###  Clone the Repository

```bash
git clone https://github.com/yourusername/ai-voice-agent.git
cd ai-voice-agent
```

---

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  Set Up Environment Variables

Create a `.env` file in the **root** folder and add:

```env
MURF_API_KEY=your_murf_api_key_here
ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

###  Run the Backend Server

```bash
uvicorn main:app --reload
```

Visit:

```
http://127.0.0.1:8000
```

---

###  Open the Frontend

Open in your browser:

```
http://127.0.0.1:8000/static/index.html
```
---

##  How It Works

1. User clicks **Record** → speaks into microphone
2. Audio is sent to **AssemblyAI** → returns transcribed text
3. Text is sent to **Google Gemini** → returns AI-generated reply
4. Reply is sent to **Murf API** → returns audio file of the response
5. Audio is played in the browser

---

##  API Endpoints

| Method | Endpoint          | Description                          |
| ------ | ----------------- | ------------------------------------ |
| POST   | `/api/agent/chat` | Send audio and get AI voice response |

---

##  Dependencies

* `fastapi`
* `uvicorn`
* `requests`
* `python-dotenv`
* `pydantic`

Install all at once:

```bash
pip install fastapi uvicorn requests python-dotenv pydantic
```



## Test the Voice Agent

Open the frontend in your browser.

Click Record → Speak → Let AI respond.

If API keys are valid, you’ll hear the AI-generated voice.



