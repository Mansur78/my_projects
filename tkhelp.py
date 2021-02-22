# import tkinter as tk
# from tkinter import messagebox
# from collections import OrderedDict
#
# class ProjectInfo(tk.Frame):
#     def __init__(self, parent, controller, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.parent = parent
#         self.controller = controller
#         self.widgets_init()
#
#     def widgets_init(self):
#         tk.Label(self,
#                     text = "Rock Controller!",
#                     width = 10,
#                     anchor = "w",
#                     justify = "left").grid(row = 0, column = 0)
#         tk.Label(self,
#                     text = "Input Name: ").grid(row = 1, column = 0)
#         self.entry = tk.Entry(self)
#         self.entry.grid(row = 1, column = 1)
#
# class ConfirmItems(tk.Frame):
#     def __init__(self, parent, frames, controller, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.parent = parent
#         self.frames = frames
#         self.controller = controller
#         self.widgets_init()
#
#     def update_entries(self):
#         self.controller.project_info.name = self.controller.project_info.entry.get()
#
#     def update_frames(self):
#         self.message = 'Click Cancel go back to reset!\n'
#         for key, values in self.frames.items():
#             for v in values:
#                 x = getattr(key, v)
#                 self.message += v + ': ' + str(x) + '\n'
#
#     def show_settings(self):
#         answer = tk.messagebox.askokcancel("Check Settings", self.message)
#         if answer in ["yes", 1]:
#             self.quit()
#
#     def combine_funcs(self, *funcs):
#         def combined_func(*args, **kwargs):
#             for f in funcs:
#                 f(*args, **kwargs)
#         return combined_func
#
#     def widgets_init(self):
#         self.cancel = tk.Button(self,
#                                 text = "Cancel",
#                                 command = self.quit)
#         self.cancel.grid(row = 0, column = 0)
#
#         self.submit = tk.Button(self,
#                                 text = "Submit",
#                                 command = self.combine_funcs(
#                                                             self.update_entries,
#                                                             self.update_frames,
#                                                             self.show_settings))
#                                 # command = lambda:[self.update_frames(), self.show_settings()]
#         self.submit.grid(row = 0, column = 1)
#
# class MainWindow(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.parent = parent
#         self.controller = self
#
#         self.project_info = ProjectInfo(self.parent, self.controller)
#         self.project_info.grid(row = 0)
#         self.widgets_init()
#
#         self.confirm_items = ConfirmItems(self.parent, self.frames, self.controller)
#         self.confirm_items.grid(row = 1)
#
#     def widgets_init(self):
#         self.dict_list = [(self.project_info, ('name',))]
#         self.frames = OrderedDict(self.dict_list)
#
# def main():
#     root = tk.Tk()
#     root.title("Welcome to Controller World!")
#     root.geometry("600x300")
#     gui = MainWindow(root)
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()

import tkinter as tk
from time import strftime

class FileMenu(tk.Menu):
    def __init__ (self, parent):
        tk.Menu.__init__(self, parent, tearoff=False)
        self.add_command(label='Exit', command=self.quit)

class MainMenu(tk.Menu):
    def __init__ (self, parent):
        tk.Menu.__init__(self, parent, tearoff=False)
        self.file_menu = FileMenu(self)
        self.add_cascade(label='Chiqish', menu=self.file_menu)



class View:
    def __init__ (self, parent):
        self.frame = tk.Frame(parent)
        self.parent = parent
        self.menu = MainMenu(self.frame)
        self.parent.configure(menu=self.menu)
        self.parent.geometry('600x200')
        self.frame.pack(fill='both', expand=True)

class App:
    def __init__ (self):
        self.root = tk.Tk()
        self.view = View(self.root)

    def run (self):
        self.root.title("O'zbekistondagi aniq vaqt!")
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()

    # def time():
    #     string = strftime("%H:%M:%S %p \n%D")
    #     label.config(text=string)
    #     label.after(1000, time)
    #
    # label = Label(root, font=("ds-digital", 50), background="black", foreground="red")
    # label.pack(anchor="center")
    # time()