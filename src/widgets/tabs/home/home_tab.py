import customtkinter as ctk
from src.widgets.tabs.home.home_content import HomeContent

from random import choice
from src.widgets.multiline_text import MultilineText


class HomeTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color='#111')
        self.content = HomeContent(self)
        self.content.place(relx=0.5, rely=0, relwidth=0.5, relheight=1, anchor='n')
