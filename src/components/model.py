from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
from src.logger import logging
from src.exceptions import CustomException
import os
import sys

class GeminiModel:
    def __init__(self):
        try:
            logging.info("Loading API key...")
            load_dotenv()
            self.GEMINI_KEY=os.getenv('GEMINI_KEY')
            logging.info("API key loaded sucessfully...")
        except Exception as e:
            logging.info("API key Loading Failed!!")
            raise CustomException(e,sys)

    def load_model(self):
        try:
            logging.info("Loading LLM Model...")
            self.model=Gemini(model='models/gemini-1.5-pro',api_key=self.GEMINI_KEY)
            return self.model
            logging.info("LLM Model loaded successfully...")
        except Exception as e:
            logging.info("LLM Model loading failed!!")
            raise CustomException(e,sys)