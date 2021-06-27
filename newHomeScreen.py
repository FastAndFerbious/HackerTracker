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
    def __init__(self, container, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Comic Sans MS", 50, 'bold'), bg="black", fg="SpringGreen2")
        lbl.place(relx=0.5, rely=0.5, anchor ="c")
        nextButton = Button(self, text="Next", fg="red", command=lambda: self.buttonPress(container))
        nextButton.pack(side=LEFT)
    def buttonPress(self, container):
        page2 = Page2(container)
        page2.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        page2.show()

#Second page asking for date
class Page2(Page):
    def __init__(self, container, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        lbl = Label(self, text="Please select today's date:  ",font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        lbl.place(relx=.5, rely=.05, anchor="c")

        #cal = Calendar(self, selectmode="day", year=2021, month=6, day=21, selectforeground='pink', foreground='yellow', highlightcolor='pink', normalforeground='orange', font=("Comic Sans MS", 20))
        cal = Calendar(self, background="black", disabledbackground="black", bordercolor="black",
                 headersbackground="black", normalbackground="black", foreground='white',
                 normalforeground='white', headersforeground='white', font=("Comic Sans MS", 20))
        cal.place(relx=.5, rely=.5, anchor="c")
        nextButton = Button(self, text="Next", fg="red", command=lambda: self.buttonPress(container, cal.get_date()))
        nextButton.pack(side=LEFT)

    def buttonPress(self, container, date):
        page3 = Page3(container, date)
        page3.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        page3.show()
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
    def __init__(self, container, date, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")                            #copy these 3 lines to make a new class
        #make checkbutton for multiselect
        lbl = Label(self, text="Select desired categories", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        lbl.place(relx=.5, rely=.05, anchor="c")

        sleep_state = IntVar()
        sleep = Checkbutton(self, text="Sleep", variable=sleep_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        sleep.place(relx=.28, rely=.2, anchor="c")

        exercise_state = IntVar()
        exercise = Checkbutton(self, text="Exercise", variable=exercise_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        exercise.place(relx=.28, rely=.3, anchor="c")

        caffeine_state = IntVar()
        caffeine = Checkbutton(self, text="Caffeine", variable=caffeine_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        caffeine.place(relx=.28, rely=.4, anchor="c")

        mood_state = IntVar()
        mood = Checkbutton(self, text="Mood", variable=mood_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        mood.place(relx=.28, rely=.5, anchor="c")

        confidence_state = IntVar()
        confidence = Checkbutton(self, text="Confidence", variable=confidence_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        confidence.place(relx=.48, rely=.2, anchor="c")

        screenTime_state = IntVar()
        screenTime = Checkbutton(self, text="Screen Time", variable=screenTime_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        screenTime.place(relx=.48, rely=.3, anchor="c")

        socializing_state = IntVar()
        socializing = Checkbutton(self, text="Socializing", variable=socializing_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        socializing.place(relx=.48, rely=.4, anchor="c")

        productivity_state = IntVar()
        productivity = Checkbutton(self, text="Productivity", variable=productivity_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        productivity.place(relx=.48, rely=.5, anchor="c")

        hygiene_state = IntVar()
        hygiene = Checkbutton(self, text="Hygiene", variable=hygiene_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        hygiene.place(relx=.68, rely=.2, anchor="c")

        categories = [sleep_state.get(), exercise_state.get(), caffeine_state.get(), mood_state.get(), confidence_state.get(), screenTime_state.get(), socializing_state.get(), productivity_state.get(), hygiene_state.get()]

        nextButton = Button(self, text="Next", fg="red", command=lambda: self.buttonPress(container, date, categories))
        nextButton.pack(side=LEFT)

    def buttonPress(self, container, date, categories):
        page4 = Page4(container, date, categories)
        page4.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        page4.show()

        #https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#Fourth Page prompting journaling input
class Page4(Page):
    def __init__(self, container, date, categories, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        choice_lbl = Label(self, text="Select Best Option", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        choice_lbl.place(relx=.5, rely=.05, anchor="c")

        sleep_label = Label(self, text="How many hours did you sleep last night?", font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        sleep_label.place(relx=.5, rely=.25, anchor="c")

        redbutton = Button(self, text="0-3 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='red', command = lambda: self.buttonPress(container, date, categories, "0-3 hours"))
        #redbutton.pack(side=LEFT)
        redbutton.place(relx=.25, rely=.5, anchor="c")

        orangeredbutton = Button(self, text="3-5 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='orange red', command = lambda: self.buttonPress(container, date, categories, "3-5 hours"))
        #greenbutton.pack(side=LEFT)
        orangeredbutton.place(relx=.37, rely=.5, anchor="c")

        orangebutton = Button(self, text="6-8 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='orange', command = lambda: self.buttonPress(container, date, categories, "6-8 hours"))
        #bluebutton.pack(side=LEFT)
        orangebutton.place(relx=.49, rely=.5, anchor="c")

        yellowbutton = Button(self, text="9-11 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow', command = lambda: self.buttonPress(container, date, categories, "9-11 hours"))
        #purpbutton.pack(side=LEFT)
        yellowbutton.place(relx=.618, rely=.5, anchor="c")

        greenbutton = Button(self, text="11+ hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='green', command = lambda: self.buttonPress(container, date, categories, "11+ hours"))
        #blackbutton.pack(side=LEFT)
        greenbutton.place(relx=.749, rely=.5, anchor="c")

    def buttonPress(self, container, date, categories, sleep):
        page5 = Page5(container, date, categories, sleep)
        page5.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        page5.show()

#Page 5 with plots
class Page5(Page):
    def __init__(self, container, date, categories, sleep, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        graph_lab = Label(self, text="Plots",  font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        graph_lab.place(relx=.5, rely=.05, anchor="c")

        nextButton = Button(self, text="Next", fg="red", command=lambda: self.buttonPress(container, date, categories, sleep))
        nextButton.pack(side=LEFT)

    def buttonPress(self, container, date, categories, sleep):
        page6 = Page6(container, date, categories, sleep)
        page6.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        page6.show()


#NLP prompting user for input
class Page6(Page):
    def __init__(self, container, date, categories, sleep, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        graph_lab = Label(self, text="How are you feeling today:", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        graph_lab.place(relx=.5, rely=.05, anchor="c")
        E1 = Entry(self)
        E1.place(relx=.5, rely=.25, anchor="c")
        blueButton = Button(self, text="Submit", bg="black", fg="white", command=lambda: self.buttonPress(container, date, categories, sleep, E1.get()))
        blueButton.place(relx=.5, rely=.35, anchor="c")

    def buttonPress(self, container, date, categories, sleep, word):
            exit()
            #To be continued

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #objects for each of the screens
        container = tk.Frame(self, bg="black")
        container.pack(side="top", fill="both", expand=True)
        home = HomePage(self, container)
        home.place(in_=container, x=50, y=50, relwidth=1, relheight=1)
        home.show()

if __name__ == "__main__":
    window = Tk()
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.title("HackerTracker")
    window.geometry('1200x600')
    window.mainloop()