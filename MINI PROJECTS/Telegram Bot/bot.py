import logging
from telegram.ext import Updater


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1803739562:AAHkk5apFkseRL55sGjjUV9t4erSPnE634k"

def main():
    upadter = Updater(TOKEN)


if __name__ == "__main__":
    main()