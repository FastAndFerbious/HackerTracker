from tkinter import *
import tkinter as tk
from tkcalendar import Calendar

import NLP

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

#home page
class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Arial Bold", 50))
        lbl.grid(column=0, row=0, sticky=E)

#Second page asking for date
class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Please select today's date:  ", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0, sticky="", columnspan=3)

        cal = Calendar(self, selectmode="day", year=2021, month=6, day=21)
        cal.place(relx=.45, rely=.5, anchor="c")

        #create spins to add date
        #month = Label(self, text="Month")
        #month.grid(column=0, row=1, sticky="")
        #spin = Spinbox(self, from_=1, to=12, width=5, format="%02.0f")
        #spin.grid(column=0, row=2, sticky="")

        #day = Label(self, text="Day")
        #day.grid(column=1, row=1, sticky="")
        #spin2 = Spinbox(self, from_=1, to=30, width=5, format="%02.0f")
        #spin2.grid(column=1, row=2, sticky="")

        #year = Label(self, text="Year")
        #year.grid(column=2, row=1, sticky="")
        #spin3 = Spinbox(self, from_=0000, to=9999, width=5, format="%04.0f")
        #spin3.grid(column=2, row=2, sticky="")        # spin3.grid(column=2, row=2, sticky="")

#Third page asking to select options

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)                            #copy these 3 lines to make a new class
        #make checkbutton for multiselect
        lbl = Label(self, text="Select desired categories", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0, sticky=N)
        sleep_state = BooleanVar()
        sleep = Checkbutton(self, text="Sleep", var=sleep_state)
        sleep.grid(column=0, row=1)
        exercise = Checkbutton(self, text="Exercise")
        exercise.grid(column=0, row=2)
        caffeine = Checkbutton(self, text="Caffeine")
        caffeine.grid(column=0, row=3)
        mood = Checkbutton(self, text="Mood")
        mood.grid(column=1, row=1)
        confidence = Checkbutton(self, text="Confidence")
        confidence.grid(column=1, row=2)
        screenTime = Checkbutton(self, text="Screen Time")
        screenTime.grid(column=1, row=3)
        socializing = Checkbutton(self, text="Socializing")
        socializing.grid(column=2, row=1)
        productivity = Checkbutton(self, text="Productivity")
        productivity.grid(column=2, row=2)
        hygiene = Checkbutton(self, text="Hygiene")
        hygiene.grid(column=2, row=3)
        #https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#Fourth Page prompting journaling input
class Page4(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        choice_lbl = Label(self, text="Select Best Option", font=("Arial Bold", 20))
        choice_lbl.pack()

        sleep_label = Label(self, text="How many hours did you sleep last night?", font=("Arial Bold", 20))
        sleep_label.pack(side=LEFT)

        redbutton = Button(self, text="0-3 hours", fg="red")
        redbutton.pack(side=LEFT)

        greenbutton = Button(self, text="3-5 hours", fg="green")
        greenbutton.pack(side=LEFT)

        bluebutton = Button(self, text="6-8 hours", fg="blue")
        bluebutton.pack(side=LEFT)

        purpbutton = Button(self, text="9-11 hours", fg="purple")
        purpbutton.pack(side=LEFT)

        blackbutton = Button(self, text="11+ hours", fg="black")
        blackbutton.pack(side=LEFT)

#Page 5 with plots
class Page5(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        graph_lab = Label(self, text="Plots", font=("Arial Bold", 20))
        graph_lab.pack(pady=10, padx=10)

#NLP prompting user for input
class Page6(Page):


    def __init__(self, *args, **kwargs):
        texts = ""
        Page.__init__(self, *args, **kwargs)
        graph_lab = Label(self, text="How are you feeling today:", font=("Arial Bold", 20))
        graph_lab.pack(pady=10, padx=10)
        E1 = Entry(self, textvariable=texts)
        E1.pack(side=TOP)
        blueButton = Button(self, text="Submit", fg="blue", command=lambda : NLP.nlp(texts.get()))
        blueButton.pack(side=TOP)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #objects for each of the screens
        home = HomePage(self)
        date = Page2(self)
        options = Page3(self)
        choices = Page4(self)
        plots = Page5(self)
        nlp = Page6(self)

        #global variables
        global screens
        screens = [home, date, options, choices, plots, nlp]
        global num
        num = 0

        #create menu
        menu = Menu(window)
        new_item = Menu(menu)
        new_item.add_command(label='Next', command=lambda: self.goNext(num))
        new_item.add_command(label='Back', command=lambda: self.goBack(num))
        new_item.add_command(label='Exit', command=lambda: self.close())
        menu.add_cascade(label='File', menu=new_item)
        window.config(menu=menu)

        #make frames
        button_frame = tk.Frame(self, bg="white")
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        #create next button
        next_btn = Button(button_frame, text="Next", bg="blue", command=lambda: self.goNext(num))
        next_btn.pack(side="right")
        #create back button
        back_btn = Button(button_frame, text="Back", bg="blue", command=lambda: self.goBack(num))
        back_btn.pack(side="left")
        #place screens into a container
        home.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        date.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        options.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        choices.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        plots.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        nlp.place(in_=container, x=50, y=50, relwidth=1, relheight=1)

        screens[0].show()

    #moves to next screen
    def goNext(self, index):
        if index < len(screens)-1:
            global num
            num += 1
            screens[index+1].show()

    #move to prev screen
    def goBack(self, index):
        if index > 0:
            global num
            num -= 1
            screens[index-1].show()

    #exits GUI
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
