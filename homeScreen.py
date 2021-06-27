from tkinter import *
import tkinter as tk
from tkcalendar import Calendar

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
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Comic Sans MS", 50, 'bold'), fg='pink')
        lbl.place(x=110, y=100)

#Second page asking for date
class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Please select today's date:  ",font=("Comic Sans MS", 40, 'bold'), fg='pink')
        lbl.place(x=120, y=0)

        cal = Calendar(self, selectmode="day", year=2021, month=6, day=21, selectforeground='pink', foreground='yellow', highlightcolor='pink', normalforeground='orange', font=("Comic Sans MS", 20))
        cal.place(relx=.45, rely=.5, anchor="c", width=500, height=230)

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
        lbl = Label(self, text="Select desired categories", font=("Comic Sans MS", 40, 'bold'), fg='pink')
        lbl.place(x=120, y=0)
        sleep_state = BooleanVar()
        sleep = Checkbutton(self, text="Sleep", var=sleep_state, font=("Comic Sans MS", 20), fg='orange')
        sleep.place(x=20, y=100)
        exercise = Checkbutton(self, text="Exercise", font=("Comic Sans MS", 20), fg='orange')
        exercise.place(x=20, y=140)
        caffeine = Checkbutton(self, text="Caffeine", font=("Comic Sans MS", 20), fg='orange')
        caffeine.place(x=20, y=180)
        mood = Checkbutton(self, text="Mood", font=("Comic Sans MS", 20), fg='orange')
        mood.place(x=20, y=220)
        confidence = Checkbutton(self, text="Confidence", font=("Comic Sans MS", 20), fg='orange')
        confidence.place(x=160, y=100)
        screenTime = Checkbutton(self, text="Screen Time", font=("Comic Sans MS", 20), fg='orange')
        screenTime.place(x=160, y=140)
        socializing = Checkbutton(self, text="Socializing", font=("Comic Sans MS", 20), fg='orange')
        socializing.place(x=160, y=180)
        productivity = Checkbutton(self, text="Productivity", font=("Comic Sans MS", 20), fg='orange')
        productivity.place(x=160, y=220)
        hygiene = Checkbutton(self, text="Hygiene", font=("Comic Sans MS", 20), fg='orange')
        hygiene.place(x=320, y=100)
        #https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#Fourth Page prompting journaling input
class Page4(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        choice_lbl = Label(self, text="Select Best Option", font=("Comic Sans MS", 50, 'bold'), fg='pink')
        choice_lbl.place(x=140, y=0)

        sleep_label = Label(self, text="How many hours did you sleep last night?", font=("Comic Sans MS", 30, 'bold'), fg='yellow')
        sleep_label.place(x=0, y=100)

        redbutton = Button(self, text="0-3 hours", fg="orange", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow')
        redbutton.pack(side=LEFT)

        greenbutton = Button(self, text="3-5 hours", fg="orange", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow')
        greenbutton.pack(side=LEFT)

        bluebutton = Button(self, text="6-8 hours", fg="orange", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow')
        bluebutton.pack(side=LEFT)

        purpbutton = Button(self, text="9-11 hours", fg="orange", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow')
        purpbutton.pack(side=LEFT)

        blackbutton = Button(self, text="11+ hours", fg="orange", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow')
        blackbutton.pack(side=LEFT)

#Page 5 with plots
class Page5(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        graph_lab = Label(self, text="Plots",  font=("Comic Sans MS", 50, 'bold'), fg='pink')
        graph_lab.pack(pady=10, padx=10)

#NLP prompting user for input
class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        graph_lab = Label(self, text="How are you feeling today:", font=("Arial Bold", 20))
        graph_lab.pack(pady=10, padx=10)
        E1 = Entry(self)
        E1.pack(side=TOP)
        blueButton = Button(self, text="Submit", fg="blue")
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
