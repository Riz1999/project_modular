import os
import sys


class CustomException(Exception):
    def __init__(self, error_message: Exception,error_details:sys):
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,
                                                                        error_details=error_details )
    
    def get_detailed_error_message(error_message: Exception,error_details:sys)-> str:
        _,_,exce_tb = error_details.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        error_message = f"""
        error occured in script:
        [{file_name}] at
        try block line number: [{try_block_line_number:}]
        """
