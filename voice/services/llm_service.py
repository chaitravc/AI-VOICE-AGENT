import logging
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class LLMService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.warning("GEMINI_API_KEY not found in .env file.")
        genai.configure(api_key=self.api_key)

    async def query_llm(self, text: str) -> str:
        """Query Gemini LLM with a single text input."""
        if not self.api_key:
            raise ValueError("Gemini API key is missing.")
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(text)
            if not response.text:
                raise ValueError("No response from Gemini LLM.")
            return response.text
        except genai.APIError as e:
            logger.error(f"Gemini API error: {str(e)}")
            raise
        except requests.RequestException as e:
            logger.error(f"Network error during LLM query: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected LLM error: {str(e)}")
            raise

    async def query_llm_with_history(self, chat_history: list) -> str:
        """Query Gemini LLM with chat history."""
        if not self.api_key:
            raise ValueError("Gemini API key is missing.")
        try:
            messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
            messages.extend(chat_history)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content("\n".join([f"{msg['role']}: {msg['content']}" for msg in messages]))
            if not response.text:
                raise ValueError("No response from Gemini LLM.")
            return response.text
        except genai.APIError as e:
            logger.error(f"Gemini API error: {str(e)}")
            raise
        except requests.RequestException as e:
            logger.error(f"Network error during LLM query: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected LLM error: {str(e)}")
            raise