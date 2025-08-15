import logging
import assemblyai as aai
from pathlib import Path
from dotenv import load_dotenv
import os
import asyncio
import requests

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class SpeechToTextService:
    def __init__(self):
        self.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        if not self.api_key:
            logger.warning("ASSEMBLYAI_API_KEY not found in .env file.")
        aai.settings.api_key = self.api_key
        self.transcriber = aai.Transcriber()

    async def transcribe_audio(self, file_path: Path) -> str:
        """Transcribe audio file using AssemblyAI."""
        if not self.api_key:
            raise ValueError("AssemblyAI API key is missing.")
        try:
            with open(file_path, "rb") as f:
                upload_url = await asyncio.to_thread(self.transcriber.upload_file, f)
            transcript = await asyncio.to_thread(self.transcriber.transcribe, upload_url)
            if not getattr(transcript, "text", None):
                raise ValueError("No transcription returned from AssemblyAI.")
            return transcript.text
        except aai.AssemblyAIError as e:
            logger.error(f"AssemblyAI error: {str(e)}")
            raise
        except requests.RequestException as e:
            logger.error(f"Network error during transcription: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected transcription error: {str(e)}")
            raise