# Fourth Page prompting journaling input
import tkinter as tk
from tkinter import *
from PageClass import Page
import spacy

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        textbox = Text(self, height=5, width=52)

        nlp = spacy.load("en_core_web_sm")
        text = ""
        doc = nlp(text)
        #capture text for NLP to parse.
        button_frame = tk.Frame(self, bg="white")
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        # create next button
        nlp_btn = Button(button_frame, text="Next", bg="blue", command=lambda: self.goNext(num))
        nlp_btn.pack(side="left")


        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop)

        textbox.insert(tk.END, text)
        textbox.pack()
        # if Page4.sleep_state is True:
        #     rad1 = Radiobutton(window, text='First', value=1)
        #     rad1.grid(column=0, row=0)