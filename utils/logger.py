# Utility module for setting up application logging
import logging

class LoggerMaker:
    @staticmethod
    def log_generator():
        logging.basicConfig(
            filename=".//logs//orangehrm.log",
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S",
            force=True # overwrite basicConfig if it was already set
        )
        logger = logging.getLogger() # get the root logger
        logger.setLevel(logging.INFO)
        return logger