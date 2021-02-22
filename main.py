from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from tes import Ui_Dialog

from tkinter import *
from tkinter.ttk import *
from time import strftime

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import tkinter as tk
import cv2
from PIL import ImageTk, Image

import qrcode

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def bp():
    ui.textEdit.setText("1 'a' синф ўқувчилари тўғрисида маълумот.\n\n"
                        "1. Aбдуллаева Азиза Каримовна. Туғилган йили 2005 йил 16 сентябрь. Манзили: Чилонзор 6 15 29"
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


ui.pushButton_3.clicked.connect(bp)


def bp():
    ui.textEdit.setText("1 'б' синф ўқувчилари тўғрисида маълумот.\n\n"
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


ui.pushButton_2.clicked.connect(bp)


def bp():
    ui.textEdit.setText("1 'а' синф рахбари.\n\n"   
                        "1. Хасанова Салима Абдуллаевна. Туғилган йили 1988 йил 16 сентябрь. Манзили: Чилонзор 6 15 29"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n1 'б' синф рахбари.\n\n"
                        "2. Aбдуллаев Тохир Мухторович. Туғилган йили 1995 йил 2 сентябрь. Манзили: Чилонзор 7 21 36"
                        " Телефон уй рақами +99871*****. Уяли алоқа воситаси:+99898*******\n\n")


ui.pushButton.clicked.connect(bp)


def bp():
    ui.textEdit.setText("Хаммага Салом. Биз Python3 дастурлаш тили орқали хамма корхона, ташкилот ва ўқув"
                        " муассасаларига енгиллик яратиш мақсадида ва маълумотларни саноқли дақиқаларда олиш "
                        "имкониятига эга электрон маълумотлар базасини яратдик. Агар Сизларни ушбу яратилган лойиха"
                        " қизиқтирса, электрон манзилимизга алоқага чиқишингиз мумкин. Эътиборингиз учун рахмат. ")


ui.pushButton_10.clicked.connect(bp)


def bp():
    ui.textEdit.setText("Привет всем. Мы создали электронную базу данных. Если вам понравился этот созданный проект"
                        " и вы заинтересованы, вы можете связаться с нами по нашему адресу электронной почты. Спасибо"
                        " за ваше внимание.")


ui.pushButton_16.clicked.connect(bp)


def bp():
    ui.textEdit.setText("2 'a' синф ўқувчилари тўғрисида маълумот.\n\n"
                        "1. Aбдуллаева Азиза Каримовна. Туғилган йили 2005 йил 16 сентябрь. Манзили: Чилонзор 6 15 29"
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


ui.pushButton_6.clicked.connect(bp)


def bp():
    ui.textEdit.setText("101 Yongin o'chirish hizmati.\n102 Police.\n103 Tez yordam.")


ui.pushButton_28.clicked.connect(bp)


def bp():
    ui.textEdit.setText("2 'а' синф рахбари.\n\n"   
                        "1. Хасанова Салима Абдуллаевна. Туғилган йили 1988 йил 16 сентябрь. Манзили: Чилонзор 6 15 29"
                        " Телефон уй рақами +99871*******. Уяли алоқа воситаси:+99898*******\n\n2 'б' синф рахбари.\n\n"
                        "2. Aбдуллаев Тохир Мухторович. Туғилган йили 1995 йил 2 сентябрь. Манзили: Чилонзор 7 21 36"
                        " Телефон уй рақами +99871*****. Уяли алоқа воситаси:+99898*******\n\n")


ui.pushButton_4.clicked.connect(bp)


def bp():
    ui.textEdit.setText("2 'б' синф ўқувчилари тўғрисида маълумот.\n\n"
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


ui.pushButton_5.clicked.connect(bp)


def bp():
    ui.textEdit.setText("Юқорида келтирилган Фамилия Исм Шарифлари мисол тариқасида келтирилган.\n Бу программа орқали"
                        " хамма керакли маълумотларни тезкорлик билан олиш имконияти яралади.\nСенсор экранли"
                        " мониторлар орқали маълумот олиш хам мумкун, фақат Windows10 платформасига уланган бўлиши"
                        " керак.\nУшбу программани Сиз хохлаган рангда, хажм(размер)да ва хар хил тилларда тайёрлаш"
                        " имкони мавжуд бўлиб, маълумотлар ўчиб кетмайди.\nАгар Сизни ушбу лойиха қизиқтирса "
                        "worldismineok@gmail.com электрон манзилига ўз таклифларингизни ёзиб  қолдиринг.\n"
                        " Эътибингиз учун рахмат. ")


ui.pushButton_25.clicked.connect(bp)


def mk():
    class Login_System:
        def __init__(self, root):
            self.root = root
            self.root.title("Shaxsiy kabinetga kirish yolagi.")
            self.root.geometry("1199x600+100+50")
            self.root.resizable(False, False)

            self.bg = ImageTk.PhotoImage(file="f2.jpg")
            self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            Frame_login = Frame(self.root, bg="blue")
            Frame_login.place(x=150, y=150, height=340, width=500)

            title = Label(Frame_login, text="Login kiriting", font=("Times new roman", 40, "bold"), fg="red",
                          bg="#373356").place(x=90, y=30)
            desc = Label(Frame_login, text="Shaxsiy kabinetga kirish", font=("Times new roman", 25, "bold"),
                         fg="yellow", bg="#373356").place(x=90, y=100)

            lbl_user = Label(Frame_login, text="Foydalanuvchi nomi", font=("Goudy old styles", 20, "bold"), fg="yellow",
                             bg="#373356").place(x=90, y=140)
            self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
            self.txt_user.place(x=90, y=170, width=350, height=35)

            lbl_pass = Label(Frame_login, text="Parol", font=("Goudy old styles", 20, "bold"), fg="yellow",
                             bg="#373356").place(x=90, y=210)
            self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
            self.txt_pass.place(x=90, y=240, width=350, height=35)

            forget_btn = Button(Frame_login, cursor="hand2", text="Parolni unutdingizmi", bg="#373356", bd=0,
                                fg="yellow", font=("times new roman", 15)).place(x=90, y=280)
            Login_btn = Button(self.root, command=self.login_function, cursor="hand2", text="LOGIN", fg="red",
                               bg="#373356", font=("times new roman", 25)).place(x=300, y=470, width=180, height=40)

        def login_function(self):
            if self.txt_pass.get() == "" or self.txt_user.get() == "":
                messagebox.showerror("Xato", "Iltimos, barcha maydonlarni to'ldiring", parent=self.root)
            elif self.txt_pass.get() != "987987" or self.txt_user.get() != "Uzb":
                messagebox.showerror("Xato", "Siz noto'g'ri foydalanuvchi nomi / parolni kiritdingiz", parent=self.root)
            else:
                messagebox.showinfo("Xush kelibsiz ",
                                    f"Xush kelibsiz {self.txt_user.get()}\nParolingiz: {self.txt_pass.get()}",
                                    parent=self.root)

    root = Tk()
    obj = Login_System(root)
    root.mainloop()


ui.pushButton_18.clicked.connect(mk)


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

    label = Label(root, font=("ds-digital", 200), background="#CA8114", foreground="red")
    label.pack(anchor="center")
    time()

    mainloop()


ui.pushButton_26.clicked.connect(soat)


sys.exit(app.exec_())
