from datetime import datetime
import traceback
import os

class Logger:

    def __init__(self, log_file, service):
       
        self.log_file = log_file
        self.service = service
        
        source_file = traceback.extract_stack()[-2][0].split("/")
        self.name = source_file[len(source_file)-1]
        

    def info(self, text):
        self.__log(text, "INFO", 36)
    
    def error(self, text):
        self.__log(text, "ERROR", 31)
        
    def warning(self, text):
        self.__log(text, "WARNING", 33)

    def critical(self, text):
        self.__log(text, "CRITICAL", 33)

    def debug(self, text):
        
        self.__log(text, "DEBUG", 34)
            

    def special(self):
        
        with open(self.log_file, "a") as f:
            formated_text = "=================================="
            
            print(formated_text)
            f.write(formated_text + "\n")


    def __log(self, text, level, color):

        source_line = traceback.extract_stack()[-3][1]
        source_function = traceback.extract_stack()[-3][2]
        
        date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        with open(self.log_file, "a") as f:

            f_service = f"{self.service}"
            f_date = f"\033[32m {date} \033[0m"
            f_level = f"\033[{color}m {level} \033[0m"
            f_source = f"\033[34m {self.name}:{source_function}:{source_line} \033[0m"
            f_text = f"\033[{color}m {text} \033[0m"

            printed_text = f"{f_service} | [ {f_date} ] | [ {f_level} ] | {f_source} | {f_text}"
            log_text = f"{self.service} | [ {date} ][ {level} ] | {self.name}:{source_function}:{source_line} | {text}"

            print(printed_text)
            f.write(log_text + "\n")
        
        
            
    def check_dir(self):

        log_file = self.log_file.split("/")
        log_file = log_file[len(log_file)-1]

        log_file_dir = self.log_file.split("/")
        log_file_dir = self.log_file.replace(log_file_dir[len(log_file_dir)-1], "")
        
        if not os.path.exists(log_file_dir):
            os.makedirs(log_file_dir)


    