import customtkinter as ctk


class ExploreContent(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(self, text='Explore')
        label.pack(expand=True, fill='both')
