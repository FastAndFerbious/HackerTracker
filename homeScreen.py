from tkinter import *
import tkinter as tk

'''def homeScreen():
    window = Tk()

    window.title("HackerTracker")
    window.geometry('1000x400')

    lbl = Label(window, text="Welcome to HackerTracker!", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)
    lbl.place(relx=.5, rely=.5, anchor="c")

    btn = Button(window, text="Click here to start!", bg="blue")
    btn.grid(column=0, row=1)
    btn.place(relx=.5, rely=.65, anchor="c")

    window.mainloop()'''

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Arial Bold", 50))
        lbl.grid(column=0, row=0, sticky=E)

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Please enter today's date:  ", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0, sticky="", columnspan=3)

        month = Label(self, text="Month")
        month.grid(column=0, row=1, sticky="")
        spin = Spinbox(self, from_=1, to=12, width=5, format="%02.0f")
        spin.grid(column=0, row=2, sticky="")

        day = Label(self, text="Day")
        day.grid(column=1, row=1, sticky="")
        spin2 = Spinbox(self, from_=1, to=30, width=5, format="%02.0f")
        spin2.grid(column=1, row=2, sticky="")

        year = Label(self, text="Year")
        year.grid(column=2, row=1, sticky="")
        spin3 = Spinbox(self, from_=0000, to=9999, width=5, format="%04.0f")
        spin3.grid(column=2, row=2, sticky="")


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)                            #copy these 3 lines to make a new class
        lbl = Label(self, text="Select 5 categories", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0, sticky=N)
        option1 = Checkbutton(self, text="option 1")
        option1.grid(column=0, row=1)
        option2 = Checkbutton(self, text="option 2")
        option2.grid(column=0, row=2)
        option3 = Checkbutton(self, text="option 3")
        option3.grid(column=0, row=3)
        option4 = Checkbutton(self, text="option 4")
        option4.grid(column=0, row=4)
        option5 = Checkbutton(self, text="option 5")
        option5.grid(column=0, row=5)
        option6 = Checkbutton(self, text="option 6")
        option6.grid(column=0, row=6)
        #https://likegeeks.com/python-gui-examples-tkinter-tutorial/

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        home = HomePage(self)
        date = Page2(self)
        options = Page3(self)

        global screens
        screens = [home, date, options]
        global num
        num = 0
        menu = Menu(window)
        new_item = Menu(menu)
        new_item.add_command(label='Next', command=lambda: self.goNext(num))
        new_item.add_command(label='Back', command=lambda: self.goBack(num))
        new_item.add_command(label='Exit', command=lambda: self.close())
        menu.add_cascade(label='File', menu=new_item)
        window.config(menu=menu)

        button_frame = tk.Frame(self, bg="white")
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        next_btn = Button(button_frame, text="Next", bg="blue", command=lambda: self.goNext(num))
        next_btn.pack(side="right")
        back_btn = Button(button_frame, text="Back", bg="blue", command=lambda: self.goBack(num))
        back_btn.pack(side="left")
        home.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        date.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        options.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        screens[0].show()

    def goNext(self, index):
        if index < len(screens)-1:
            global num
            num += 1
            screens[index+1].show()

    def goBack(self, index):
        if index > 0:
            global num
            num -= 1
            screens[index-1].show()

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