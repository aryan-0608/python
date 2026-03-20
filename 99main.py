# import os
# import time

# REPEAT_INTERVAL = 10  # Time in seconds (1 hour)

# while True:
#     command = "osascript -e \ 'say \"Hey Aryan drink water\"\';osascript -e \'display alert \"Hey Aryan drink water\"\'"
#     os.system(command)
#     time.sleep(REPEAT_INTERVAL)  # Wait for the specified
#  interval before the next alert

import pyttsx3
import time

engine = pyttsx3.init()

while True:
    engine.say("Hey Aryan, drink water")
    engine.runAndWait()
    time.sleep(10)   # 10 seconds baad fir bolega