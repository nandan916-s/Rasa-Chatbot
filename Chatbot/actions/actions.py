
import logging
from typing import Any, Text, Dict, List
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
import string

logging.basicConfig(level=logging.DEBUG)

class ActionGreet(Action):
    def name(self):
        return "action_PN_2_save_name"

    def run(self, dispatcher, tracker, domain):
        intros = ["im ", "i am ", "i am called ", "im called ", "call me "]
        name = ""
        stripped = ""
        sentence = (tracker.latest_message)['text']
        exclude = set(string.punctuation)
        stripped = stripped.join(ch for ch in sentence if ch not in exclude).lower()
        for intro in intros:
            if re.search(intro, stripped):
                name = stripped.split(intro)[1]
                name = name.title()
        if name is "":
            name = sentence.title()
        logging.debug("*** ActionGreet: Name saved as: " + name)
        return [SlotSet("name", name)]
