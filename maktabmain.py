# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from maktab import Ui_Form
import json

from tkinter.ttk import *
from time import strftime

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import tkinter as tk
import cv2
from PIL import ImageTk, Image

import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import random


app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def bp():
    ui.textEdit.setText("1 'а' синф ўқувчилари тўғрисида маълумот.\n\n"
                        "1. Дониёрова Салима Каримовна. Туғилган йили 2005 йил 16 сентябрь. Манзили: Чилонзор 6 15 29"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n"
                        "2. Aбдуллаев Тохир Мухторович. Туғилган йили 2005 йил 2 сентябрь. Манзили: Чилонзор 7 21 36"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n"
                        "3. Иноғомов Салим Тоирович. Туғилган йили 2005 йил 2 сентябрь. Манзили: Чилонзор 7 21 36"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n"
                        "4. Aбдуллаева Азиза Каримовна. Туғилган йили 2005 йил 16 сентябрь. Манзили: Чилонзор 6 15 29"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n"
                        "5. Aбдуллаев Тохир Мухторович. Туғилган йили 2005 йил 2 сентябрь. Манзили: Чилонзор 7 21 36"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n"
                        "6. Иноғомов Салим Тоирович. Туғилган йили 2005 йил 2 сентябрь. Манзили: Чилонзор 7 21 36"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n")


ui.pushButton_8.clicked.connect(bp)


def assist():
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
            say("Из Пахты и я сосед Алижана Бектурова")
        elif command == "адрес азиза":
            say("город ташкент чиланзарский район квартал8 дом25 квартира49")
        elif command == "ты дура":
            say("нет я не дура а умница")
        elif command == "кто создал тебя":
            say("мой создатель")
        elif command == "для чего ты создана":
            say("Чтобы помочь людям")
        elif command == "данные пятый дом 23":
            say("оформлен гражданину Маматову прописан 3 человек телефон 998 97 758 92 22 повторяю 998 90 554 444 ")
        elif command == "спасибо":
            say("незачто")
        elif command == "на каких языках разговариваешь":
            say("на всех, только нужна разрешение моего создателя")
        elif command == "где али":
            say("я не знаю где он если очень важно позвони ему или спроси у марины  ")
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


ui.pushButton_53.clicked.connect(assist)


def soat():

    root = Tk()

    button = Button(root, text="Click me!")
    img = PhotoImage()  # make sure to add "/" not "\"
    button.config(image=img)
    button.pack()  # Displaying the button
    root.title("O'zbekistondagi aniq vaqt!")
    root.geometry("1199x600+100+50")

    def time():
        string = strftime("%H:%M:%S  \n%D")
        label.config(text=string)
        label.after(1000, time)

    label = Label(root, font=("ds-digital", 200), background="#00007f", foreground="red")
    label.pack(anchor="center")
    time()

    mainloop()


ui.pushButton_63.clicked.connect(soat)


def mk():
    class Login_System:
        def __init__(self, root):
            self.root = root
            self.root.title("1 A sinf to'grisida ma'lumot.")
            self.root.geometry("1210x680+100+50")
            self.root.resizable(False, False)

            self.bg = ImageTk.PhotoImage(file="f2.jpg")
            self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            Frame_login = Frame(self.root, bg="blue")
            Frame_login.place(x=50, y=50, height=1400, width=1000)

            desc = Label(Frame_login, text="Dushanba\n1 'a' dars jadvali. 1. O'qish 2. Matem\n1 'b' dars jadvali. 1. "
                                           "O'qish 2. Matem\nПонидельник\n 1 'a' класс 1. Матем 2. Узбексий язык\n 1 "
                                           "'б' класс 1. Матем 2. Узбексий язык\nSeshanba\n1 'a' dars jadvali. 1. "
                                           "O'qish 2. Matem\n1 'b' dars jadvali. 1. "
                                           "O'qish 2. Matem\nВторник\n 1 'a' класс 1. Матем 2. Узбексий язык\n 1 "
                                           "'б' класс 1. Матем 2. Узбексий язык\nChorshanba\n1 'a' dars jadvali. 1."
                                           " O'qish 2. Matem\n1 'b' dars jadvali. 1. "
                                           "O'qish 2. Matem\nСреда\n 1 'a' класс 1. Матем 2. Узбексий язык\n 1 "
                                           "'б' класс 1. Матем 2. Узбексий язык\nPayshanba\n1 'a' dars jadvali. 1. "
                                           "O'qish 2. Matem\n1 'b' dars jadvali. 1. "
                                           "O'qish 2. Matem\nЧетверг\n 1 'a' класс 1. Матем 2. Узбексий язык\n 1 "
                                           "'б' класс 1. Матем 2. Узбексий язык\nJuma\n1 'a' dars jadvali. 1. O'qish 2."
                                           " Matem\n1 'b' dars jadvali. 1. "
                                           "O'qish 2. Matem\nПятница\n 1 'a' класс 1. Матем 2. Узбексий язык\n 1 "
                                           "'б' класс 1. Матем 2. Узбексий язык\nShanba\n1 'a' dars jadvali. 1. O'qish"
                                           " 2. Matem\n1 'b' dars jadvali. 1. O'qish 2. Matem1. O'qish 2. Matem1. "
                                           "O'qish 2. Matem\nСуббота\n 1 'a' класс 1. Матем 2. Узбексий язык\n 1 "
                                           "'б' класс 1. Матем 2. Узбексий язык", font=("Times new roman", 11),
                         fg="yellow", bg="#373356").place(x=20, y=1)

    root = Tk()
    obj = Login_System(root)
    root.mainloop()


ui.pushButton_26.clicked.connect(mk)


def hizmat():
    class Login_System:
        def __init__(self, root):
            self.root = root
            self.root.title("1 A sinf to'grisida ma'lumot.")
            self.root.geometry("1210x680+100+50")
            self.root.resizable(False, False)

            self.bg = ImageTk.PhotoImage(file="f2.jpg")
            self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            Frame_login = Frame(self.root, bg="blue")
            Frame_login.place(x=50, y=50, height=1400, width=1000)

            desc = Label(Frame_login, text="O't o'chirish hizmati  --  101\n\nIIB  --  102\n\nTez yordam  --  103\n\n"
                                           "Пожарная служба  --  101\n\nМилиция  --  102\n\nСкорая помощь  --  103\n\n"
                                           "", font=("Times new roman", 20),
                         fg="yellow", bg="#373356").place(x=20, y=1)

    root = Tk()
    obj = Login_System(root)
    root.mainloop()


ui.pushButton_44.clicked.connect(hizmat)


sys.exit(app.exec_())
