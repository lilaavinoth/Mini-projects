import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak')
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source)
    text = r.recognize_google(audio)
    print(text)
    textspeek = gTTS(text=text,lang='en',slow=False)
    s


