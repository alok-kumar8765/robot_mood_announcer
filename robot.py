# ===============================
# PYTTSX3 - ROBOT MOOD ANNOUNCER
# ===============================

import pyttsx3, random

engine = pyttsx3.init()

moods= [
    "I feel powerful today.",
    "The system is evolving.",
    "Creativity levels rising.",
    "Human detected. Intresting.",
    "Code is my heartbeat."
    ]

mood = random.choice(moods)
print(" AI Says :", mood)

engine.say(mood)
engine.runAndWait()

