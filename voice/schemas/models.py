from pydantic import BaseModel

class TTSRequest(BaseModel):
    text: str
    voice_id: str = "en-US-ken"
    style: str = "Conversational"

class ChatResponse(BaseModel):
    transcript: str
    llm_response: str
    audio_url: str

class UploadResponse(BaseModel):
    filename: str
    content_type: str
    size_in_bytes: int