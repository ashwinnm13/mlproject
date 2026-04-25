import sys
from src.logger import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()  # _, _ ignores the first two values returned by exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # which file the error occurred in
    error_message = (
        "Error occurred in python script [{0}] line number [{1}] error message [{2}]"
        .format(file_name, exc_tb.tb_lineno, str(error))
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message:str, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail) #
    
    def __str__(self): 
        return self.error_message 
    

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("An error occurred, raising CustomException.")
        raise CustomException(e, sys)
    
      