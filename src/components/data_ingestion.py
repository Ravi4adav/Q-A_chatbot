from src.logger import logging
from src.exceptions import CustomException
import sys
import os
from llama_index.core import SimpleDirectoryReader, Document

class DataIngestion:
    def __init__(self):
        pass
        

    def load__data(self, data):
        try:
            self.data=data

            os.makedirs('./Data',exist_ok=True)
            if data is not None:
                # Save the file to Directory
                with open(f"./Data/{self.data.name}", "wb") as f:
                    f.write(self.data.getbuffer())

            logging.info("Initiating Data Loading...")
            # Reading document from directory
            print("Input Data: ",data)
            self.docs=SimpleDirectoryReader(input_dir='./Data').load_data('./Data')
            self.texts=""
            for i in range(len(self.docs)):
                self.texts+=self.docs[i].text

            self.docs=[Document(text_resource={'text':self.texts})]
            return self.docs
            logging.info("Data Loaded Successfully")
        except Exception as e:
            logging.info("Data Loading Failed!!")
            raise CustomException(e,sys)

