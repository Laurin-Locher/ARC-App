import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window configuration
        self.title('ARC App')
        self.geometry('1000x800')

        # run
        self.mainloop()
