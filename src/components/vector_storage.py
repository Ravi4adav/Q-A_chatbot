from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
import sys
from src.exceptions import CustomException
from src.logger import logging

class StorageVectorIndex:
    def __init__(self, model, embed_model, docs):
        try:
            logging.info("Setting Gemini model, embeddings and transformation default...")
            self.docs=docs
            # print("Docs from Vectora storage file: ",self.docs)
            
            self.embed_model=embed_model
            self.transformations=[SentenceSplitter(chunk_overlap=20, chunk_size=1024)]
            logging.info("Gemini model, embeddings and transformation setup as  default...")
        except Exception as e:
            logging.info("Gemini model, embeddings and transformation Failed to setup as  default!!")
            raise CustomException(e,sys)

    def get_vector_index(self):
        try:
            logging.info("Initializing Storage Vector Indexing...")
            # Settings.llm=self.model
            Settings.embed_model=self.embed_model
            Settings.transformations=[SentenceSplitter(chunk_overlap=20, chunk_size=1024)]
            self.index=VectorStoreIndex.from_documents(documents=self.docs,embed_model=Settings._embed_model,transformations=Settings._transformations ,show_progress=True)
            
            return self.index
            logging.info("Vector Storage Indexing Successfully...")
        except Exception as e:
            logging.info("Vector Storage Indexing Failed!!")
            raise CustomException(e,sys)