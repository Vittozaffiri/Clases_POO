from fileinput import filename
import logging

logging.basicConfig(
    filename = "clase.log",
    encoding="utf-8",
    level = logging.DEBUG
)

logging.warning("Este es un warning")
logging.info("el programa paso por aca")
logging.critical("Pasó un desastre")