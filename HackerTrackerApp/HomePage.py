from tkinter import *
from PageClass import Page


# home page
class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Arial Bold", 50))
        lbl.grid(column=0, row=0, sticky=E)  # testing





