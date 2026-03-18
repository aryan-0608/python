# For Mac
# from os import system
# from tkinter.font import names
# names = ["Aryan","pradeep","Bablu","Mangle"]
# for name in names:
#     system(f'say {name}')


import pyttsx3

engine = pyttsx3.init()

names = ["Aryan", "Pradeep", "Bablu", "Mangle"]

for name in names:
    engine.say(names)

engine.runAndWait()
