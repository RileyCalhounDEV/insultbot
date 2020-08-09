import random
from gtts import gTTS
from playsound import playsound
import urllib.request as urllib
import time

lastText = 'boop'
keepGoing = True

def generateFiles():
    url = 'https://gist.githubusercontent.com/RileyCalhounDEV/cdc1f31e1f0f27ebb6192b74e814f2ca/raw/eefaf0a47383a81b4fa6c513569b2e170ed0f05d/insults'
    f = urllib.urlopen(url)
    text = str(f.read())
    text = text.replace("b", "")
    text = text.replace("\"", "")
    text = text.replace("\\n", ", ")
    textList = text.split(", ")
    for t in textList:
        tts = gTTS(t)
        tts.save("sounds/" + t + ".mp3")

def read():
    url = 'https://gist.githubusercontent.com/RileyCalhounDEV/cdc1f31e1f0f27ebb6192b74e814f2ca/raw/1bacaca746d6583fe12fcf04f0bd023bbe11fb40/insults'
    f = urllib.urlopen(url)
    text = str(f.read())
    text = text.replace("b", "")
    text = text.replace("\"", "")
    text = text.replace("\\n", ", ")
    textList = text.split(", ")
    t = random.choice(textList)
    playsound("sounds/" + t + ".mp3")
    print(t)

generateFiles()
while(keepGoing):
    read()
    time.sleep(60 * 10)