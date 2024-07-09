import customtkinter as ctk


class GameTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color='red')

        label = ctk.CTkLabel(self, text='Game')
        label.pack(expand=True, fill='both')

