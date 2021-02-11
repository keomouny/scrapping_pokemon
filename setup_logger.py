import logging
import os

logging.basicConfig(filename=f"{os.getcwd()}/logs/log.log", filemode="w",
                    format="%(asctime)s - %(message)s", datefmt="%m/%d/%Y %I:%M%S %p", level=logging.DEBUG)

logger = logging.getLogger(__name__)
