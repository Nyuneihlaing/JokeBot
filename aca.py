import logging
import os
import re

from dotenv import load_dotenv
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_APP_TOKEN = os.environ["Socket_Mode_Token"]
SLACK_BOT_TOKEN = os.environ["Bot_User_OAuth_Token"]

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")

@app.event("app_mention")
def event_test(event, say):
    say(f"Hi there, <@{event['user']}>!")

@app.message(re.compile("^joke$"))
def show_random_joke(message, say):
    dm_channel = message["channel"]

    joke = pyjokes.get_joke()

    say(text=joke, channel=dm_channel)  


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
