import logging
from pathlib import Path

def logger_setup(log_name: str, log_level=logging.DEBUG):
    # Create log directory
    log_dir = Path("log")
    log_dir.mkdir(parents=True, exist_ok=True)

    # Configure logging
    log_file = log_dir / (log_name + ".log")
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # Output to console
        ]
    )

    return logging.getLogger(log_name)

# def main():
#     print(" ===== Start to test logger =====")
#     logger = logger_setup("logger_test")
#     logger.debug("Test 0")
#     logger.info("Test 1")
#     logger.warning("Test 2")
#     logger.fatal("Test 3")
#     logger.error("Test 4")
#     print(" ===== End to test logger =====")

# if __name__ == "__main__":
#     main()