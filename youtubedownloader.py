from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *


# font
font = ('verdana', 20)
original_font = ('Courier', 12)
file_size = 0

# switch function:
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="#CECCBE", activebackground="#CECCBE")
        root.config(bg="#CECCBE")
        txt.config(text="Faol holat: OFF", bg="#CECCBE")
        btnState = False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="#2B2B2B")
        txt.config(text="Faol holat: ON", bg="#2B2B2B")
        btnState = True


# on complete callback function
def completeDownload(stream=None, file_path=None):
    print("yuklab olish tugallandi")
    showinfo("Message", "Fayl yuklab olindi...")
    downloadBtn['text'] = "Videoni yuklab olish"
    downloadBtn['state'] = "active"
    url_entry.delete(0, END)


# on progress callback function
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    downloadBtn['text'] = "{:00.0f}% downloaded ".format(percent)


# download function
def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        print("something went wrong")


def btnClicked():
    try:
        downloadBtn['text'] = "Iltimos kuting..."
        downloadBtn['state'] = 'disabled'
        url = url_entry.get()
        if url == '':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
        print(e)


# gui coding
root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("img/icon.ico")
root.geometry("850x550")

# switch
btnState = False

# switch images:
onImg = PhotoImage()#(file="img/onbutton.png")
offImg = PhotoImage()#(file="img/offbutton.png")

# Night Mode:
txt = Label(root, text="Faol holat: ON", font=" 20", bg="#CECCBE", fg="green")
txt.pack(side='bottom')

# switch widget:
btn = Button(root, text="OFF", borderwidth=0, command=switch, bg="#CECCBE", activebackground="#CECCBE", pady=1)
btn.pack(side=BOTTOM, padx=10, pady=10)
btn.config(image=offImg)

# main icon section
file = PhotoImage(file="img/youtube.png")
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)

# Url Field
url_entry = Entry(root, justify=CENTER, bd=5, fg='#FF191D')
url_entry.pack(side=TOP, fill=X, padx=10)
url_entry.focus()

# download button
downloadBtn = Button(root, text="Videoni yuklab olish", font=font, relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()
