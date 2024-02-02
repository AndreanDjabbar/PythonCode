import os
import logging

data_location = "DATA"
file_name = "data.txt"
data_path = os.path.join(data_location, file_name)
# Path for data file location

log_location = "LOG"
activity_log = "activity.log"
error_log = "error.log"

activity_path = os.path.join(log_location, activity_log)
error_path = os.path.join(log_location, error_log)

activity_handler = logging.FileHandler(activity_path)
error_handler = logging.FileHandler(error_path)

formatter = logging.Formatter(
    "%(name)s | %(levelname)s | %(message)s | %(asctime)s",
    datefmt="%d - %b - %y %H:%M:%S"
)
# Formatter for logger

activity_handler.setFormatter(formatter)
# Set formatter for Activity Handler
error_handler.setFormatter(formatter)
# Set formatter for Error Handler

activity_logger = logging.getLogger(f"ACTIVITY LOGGER({__name__})")
activity_logger.setLevel(logging.INFO)
activity_logger.addHandler(activity_handler)

def clear_data():
    # Delete all Data from file data.txt
    activity_logger.info("Clearing File data.txt")
    with open(data_path, 'w', encoding="utf-8") as f:
        f.write("")