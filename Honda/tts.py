from gtts import gTTS
import os
from playsound import playsound

upload_response = "this is a test"

language = 'en'
myobj = gTTS(text=upload_response, lang=language, slow=False)
myobj.save("response.mp3")
playsound("response.mp3")