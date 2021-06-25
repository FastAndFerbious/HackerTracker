from tkinter import *
import tkinter as tk
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
from HomePage import HomePage

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # objects for each of the screens
        home = HomePage(self)
        date = Page1(self)
        options = Page2(self)
        choices = Page3(self)

        # global variables
        global screens
        screens = [home, date, options, choices]
        global num
        num = 0

        # create menu
        menu = Menu(window)
        new_item = Menu(menu)
        new_item.add_command(label='Next', command=lambda: self.goNext(num))
        new_item.add_command(label='Back', command=lambda: self.goBack(num))
        new_item.add_command(label='Exit', command=lambda: self.close())
        menu.add_cascade(label='File', menu=new_item)
        window.config(menu=menu)

        # make frames
        button_frame = tk.Frame(self, bg="white")
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        # create next button
        next_btn = Button(button_frame, text="Next", bg="blue", command=lambda: self.goNext(num))
        next_btn.pack(side="right")
        # create back button
        back_btn = Button(button_frame, text="Back", bg="blue", command=lambda: self.goBack(num))
        back_btn.pack(side="left")
        # place screens into a container
        home.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        date.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        options.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        choices.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        screens[0].show()

    # moves to next screen
    def goNext(self, index):
        if index < len(screens) - 1:
            global num
            num += 1
            screens[index + 1].show()

    # move to prev screen
    def goBack(self, index):
        if index > 0:
            global num
            num -= 1
            screens[index - 1].show()

    # exits GUI
    def close(self):
        window.destroy()
        exit()


if __name__ == "__main__":
    window = Tk()
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.title("HackerTracker")
    window.geometry('1000x400')
    window.mainloop()
