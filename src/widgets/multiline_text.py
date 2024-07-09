import customtkinter as ctk
from  src.settings import Settings


class MultilineText(ctk.CTkFrame):
    def __init__(self, master, text, text_color='white', fg_color='black', justify='left'):
        super().__init__(master)

        self.label = ctk.CTkLabel(self,
                                  text=text,
                                  fg_color=fg_color,
                                  justify=justify,
                                  text_color=text_color,
                                  font=Settings.body_format
                                  )
        self.label.bind('<Configure>', self.update_wrap_length)

        self.label.pack(expand=True, fill='both')

    def update_wrap_length(self, event):
        self.label.configure(wraplength=self.label.winfo_width())
