from random import randint
from flask import Flask, request
import logging
import psutil

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# https://opentelemetry.io/docs/languages/python/getting-started/
@app.route("/rolldice")
def roll_dice():
    player = request.args.get('player', default=None, type=str)
    result = str(roll())
    if player:
        logger.warning("%s is rolling the dice: %s", player, result)
    else:
        logger.warning("Anonymous player is rolling the dice: %s", result)
    return result


def roll():
    return randint(1, 6)

@app.route('/resources')
def cpu_util():
    cpu_percents = psutil.cpu_percent(interval=1, percpu=True)
    cpu_core_count = psutil.cpu_count()
    # cpu_phys_count = psutil.cpu_count(logical=False)
    return f"""
    CPU utilization: {cpu_percents}
    CPU core count: {cpu_core_count}
    """
