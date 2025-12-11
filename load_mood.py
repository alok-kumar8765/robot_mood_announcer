import json, random, pyttsx3

with open("moods.json", "r") as file:
    mood_data = json.load(file)

all_moods = (
    mood_data["system_moods"] +
    mood_data["emotional_moods"] +
    mood_data["advanced_ai_moods"] +
    mood_data["funny_moods"] +
    mood_data["robotic_moods"]
)

mood = random.choice(all_moods)

engine = pyttsx3.init()
print("🤖:", mood)
engine.say(mood)
engine.runAndWait()
