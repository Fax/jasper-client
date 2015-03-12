# -*- coding: utf-8-*-
import datetime
import re
from client.app_utils import getTimezone
from semantic.dates import DateService
from chatterbot import ChatBot

WORDS = ["CHAT"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    mic.say("Chatterbot is starting now")
    handleForever(mic, profile)
    mic.say("Chatterbot is stopping now")


def handleForever(mic, profile):
    chatbot = ChatBot()

    while True:
        exitfromhere = False
        input = mic.activeListen()
        if input == "exit":
            return
        mic.say(chatbot.get_response(input))


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\chat\b', text, re.IGNORECASE))
