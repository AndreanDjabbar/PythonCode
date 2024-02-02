import logging

# logging.info("INfo masse")
# logging.debug("DEBugggg")
# logging.warning("WaRNINGHGGG")
# logging.error("ERORRRR")
# logging.critical("Crittt")

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(message)s - %(levelname)s",
    datefmt="%m-%b-%y"
)

logging.debug("Debug Bos")
logging.warning("Warning Bos")
logging.error("Error Bos")
logging.critical("Critical Bos")