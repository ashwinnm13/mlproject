import logging
import os
from datetime import datetime

# Create log file name
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create logs folder path
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Correct full file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Configure the logging system for the entire project
# filename: Logs will be saved to the specified file path instead of printing in console
# format: Defines how each log message should look
#   %(asctime)s  -> Timestamp (when the log was created)
#   %(levelname)s -> Type of log (INFO, WARNING, ERROR, etc.)
#   %(message)s   -> Actual log message
# level: Sets the minimum level of logs to capture
# logging.INFO means it will capture INFO, WARNING, ERROR, and CRITICAL (but not DEBUG)

if __name__ == "__main__":
    logging.info("This is an info log message.")
    logging.warning("This is a warning log message.")
    logging.error("This is an error log message.")

