import os
import logging
import traceback

from src.processor import processEvt

log = logging.getLogger("handler")
if os.getenv("LOG_LEVEL") == "INFO":
    logging.basicConfig(level=logging.INFO) ##keep it simple for prod
else:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s',
                        level=logging.DEBUG,
                        datefmt='%m/%d/%Y %I:%M:%S %p')


def lambda_handler(evt, ctx):
    if evt:
        failedmessages = []  # Implementing partial batch responses
        response = {}

        for r in evt["Records"]:  ## process batch of events
            body = r["body"]  # its escaped json
            log.debug(f"SQS Message Body: {body}")

            try:
                response = processEvt(body)  # process single event here
                log.info(response)
            except Exception as e:
                print(traceback.format_exc())
                failedmessages.append({"itemIdentifier": r['messageId']})

        response["batchItemFailures"] = failedmessages
        response["success"] = len(failedmessages) == 0
        log.info("Done processing " + str(response))
        return response
