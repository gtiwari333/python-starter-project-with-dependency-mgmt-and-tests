import json
import logging
import unittest

from src.handler import lambda_handler

log = logging.getLogger("test-handler")
logging.basicConfig(format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class TestFunction(unittest.TestCase):
    def test_function(self):
        file = open('test/event.json', 'rb')
        try:
            event = json.load(file)
            result = lambda_handler(event, {'messageId': '1234'})
            log.info("Result " + str(result))

            self.assertEqual(str(result), "{'result': 54, 'batchItemFailures': [], 'success': True}")
        finally:
            file.close()


if __name__ == '__main__':
    unittest.main()
