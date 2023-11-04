import logging
import json
from src.handler import lambda_handler

log = logging.getLogger("runner")
logging.basicConfig(level=logging.DEBUG)

def run():
    file = open('test/event.json', 'rb') ## pick file from test/ folder
    try:
        event = json.load(file)
        result = lambda_handler(event, {'messageId': '1234'})
        log.info("Result " + str(result))
    finally:
        file.close()


if __name__ == '__main__':
    run()
