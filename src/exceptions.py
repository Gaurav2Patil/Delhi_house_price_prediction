import sys
import logging

def error_msg_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_massage = "Error details:\n Sript_name:[{0}] \nLine_number:[{1}] \nError:[{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_massage

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_massage = error_msg_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_massage
