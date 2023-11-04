import os
import logging
import json
import yaml

log = logging.getLogger("processor")

# read profile and corresponding yaml
profile = os.environ.get("PROFILE") or "dev"

with open(f"src/config/{profile}.yaml") as properties:
    config = yaml.safe_load(properties)


def processEvt(body):
    log.info("Running with profile " + profile)

    payload = json.loads(body)

    a = payload["a"]
    b = config["app"]["b"]
    c = int(a) + int(b)

    log.info("Result " + str(c))

    return {"result": c}
