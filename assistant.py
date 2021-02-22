import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import random
import urllib3


urllib3.disable_warnings()

def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то...")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        print(f"Вы сказали: {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return "Ошибка распознание"
    except sr.RequestError:
        return "Ошибка запроса"


def say(text):
    voice = gTTS(text, lang="ru")
    unique_file = "audio" + str(random.randint(0, 10000)) + ".mp3"
    voice.save(unique_file)

    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f"Ассистент: {text}")


def handle_command(command):
    command = command.lower()

    if command == "привет":
        say("привет как дела")
    elif command == "кто ты":
        say("Иона")
    elif command == "ты откуда":
        say("Из Ташкента")
    elif command == "адрес азиза":
        say("город ташкент чиланзарский район квартал8 дом25 квартира49")
    elif command == "ты дура":
        say("нет я не дура а умница")
    elif command == "кто создал тебя":
        say("мой создатель")
    elif command == "для чего ты создана":
        say("Чтобы помочь людям")
    elif command == "мне нужун номер али":
        say("запиши 999 95 554 444 повторяю 999 95 544 444")
    elif command == "спасибо":
        say("незачто")
    elif command == "на каких языках разговариваешь":
        say("на всех, только нужна разрешение моего создателя")
    elif command == "где али":
        say("я не знаю где он если очень важно позвони ему")
    elif command == "пока":
        stop()
    else:
        say("Не понятно, повторите")


def stop():
    say("До скорого")
    exit()


def start():
    print("Запуск ассистента...")

    while True:
        command = listen()
        handle_command(command)


try:
    start()
except KeyboardInterrupt:
    stop()
 #"Ea6YAzS-8yS5otTQR7aXKGDEyrYqgLL28Nt6OYeo"
