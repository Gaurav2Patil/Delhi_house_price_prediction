import logging 
import datetime as datetime
import os 

Log_File = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"
log_path = os.path.join("src\Delhi_House_Price_Prediction","logs", Log_File)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,Log_File)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)s %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

if __name__ == "__main__":
    logging.info("Starting Log.")