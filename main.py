import datetime
import webbrowser

import speech_recognition as sr
import os
from openai import OpenAI
from config import apikey
import random

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Burhan: {query}\n JinAI: "
    client = OpenAI(api_key=apikey)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": chatStr
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response.choices[0].message.content)
    chatStr += f"{response.choices[0].message.content}\n"
    return response.choices[0].message.content

def ai(prompt):
    text = f"OpenAI response for prompt: {prompt} \n ******************************* \n\n"
    client = OpenAI(api_key=apikey)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response.choices[0].message.content
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:50]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error Occurred. Sorry for inconvenience"


if __name__ == '__main__':
    print("Welcome to JinAI")
    say("Welcome to Jin A.I. ....")
    while True:
        print("listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "/Users/burhan/Downloads/takemehome.mp3"
            os.system(f"open {musicPath}")
        elif "what is the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"sir the current time is {strfTime}....")
        elif "using artificial intelligence".lower() in query.lower():
            print("ai")
            ai(prompt=query)
        elif "quit" in query.lower():
            exit()
        elif "reset chat" in query.lower():
            chatStr = ""
        else:
            print("chatting...")
            chat(query)

