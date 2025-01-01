from llama_index.embeddings.gemini import GeminiEmbedding
from dotenv import load_dotenv
from src.exceptions import CustomException
from src.logger import logging
import sys
import os

class GeminiEmbedings:
    def __init__(self):
        try:
            logging.info("Loading API key...")
            load_dotenv()
            self.GEMINI_KEY=os.getenv('GEMINI_KEY')
            logging.info("API key loaded sucessfully...")
        except Exception as e:
            logging.info("API key Loading Failed!!")
            raise CustomException(e,sys)

    def load_embeddings(self):
        try:
            logging.info("Loading Embedding layer...")
            self.embed_model_name = "models/embedding-001"
            self.embed_model = GeminiEmbedding(model_name=self.embed_model_name, api_key=self.GEMINI_KEY)
            return self.embed_model
            logging.info("Embedding Layer loaded successfully...")
        except Exception as e:
            logging.info("Embedding Layer Loading Failed!!")
            raise CustomException(e,sys)