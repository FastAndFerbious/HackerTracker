from tkinter import *
from PageClass import Page

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)  # copy these 3 lines to make a new class
        # make checkbutton for multiselect
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
        # https://likegeeks.com/python-gui-examples-tkinter-tutorial/
