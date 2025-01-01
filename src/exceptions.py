import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_msg, error: sys):
        super().__init__(error_msg)
        _,_,tb=error.exc_info()
        tb_info=traceback.extract_tb(tb)[-1]
        self.filename=tb_info.filename
        self.line_no=tb_info.lineno
        self.error_msg=error_msg


    def __str__(self):
        return (f"\n"
                f"Filepath: {self.filename} \n"
                f"Line no: {self.line_no} \n"
                f"Error: {self.error_msg}")

