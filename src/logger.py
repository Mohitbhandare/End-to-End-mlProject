import logging
import os
from datetime import datetime

# log is created
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# file path of the logger
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# formate of the log
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# for testing
# if __name__ == "__main__":
#     logging.info("logging has started")