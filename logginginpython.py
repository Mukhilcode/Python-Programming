import logging
import os

#create a logger string

logging_string="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder="logs"
log_file="logs/running_log.log"
os.makedirs(log_folder,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_string,
    handlers=[
        logging.FileHandler(log_file)
    ]

)
logger=logging.getLogger("mylog")


def add_number(a,b):
    out=a+b
    logger.info("succesfully executed")
    return out


num =add_number(4,34)
print(num)