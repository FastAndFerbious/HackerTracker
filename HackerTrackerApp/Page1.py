from tkinter import *
from PageClass import Page
from tkcalendar import Calendar


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = Label(self, text="Please select today's date:  ", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0, sticky="", columnspan=3)

        cal = Calendar(self, selectmode="day", year=2021, month=6, day=21)
        cal.place(relx=.45, rely=.5, anchor="c")

        # create spins to add date
        # month = Label(self, text="Month")
        # month.grid(column=0, row=1, sticky="")
        # spin = Spinbox(self, from_=1, to=12, width=5, format="%02.0f")
        # spin.grid(column=0, row=2, sticky="")

        # day = Label(self, text="Day")
        # day.grid(column=1, row=1, sticky="")
        # spin2 = Spinbox(self, from_=1, to=30, width=5, format="%02.0f")
        # spin2.grid(column=1, row=2, sticky="")

        # year = Label(self, text="Year")
        # year.grid(column=2, row=1, sticky="")
        # spin3 = Spinbox(self, from_=0000, to=9999, width=5, format="%04.0f")
        # spin3.grid(column=2, row=2, sticky="")        # spin3.grid(column=2, row=2, sticky="")

# Third page asking to select options
