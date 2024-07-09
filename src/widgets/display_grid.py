import customtkinter as ctk
from src.settings import Settings


class DisplayGrid(ctk.CTkFrame):
    def __init__(self, master, input_data):
        super().__init__(master)
        self.data = input_data

        self.width_in_fields = len(input_data[0])
        self.height_in_fields = len(input_data)

        for row in range(self.height_in_fields):
            self.rowconfigure(row, weight=1, uniform='a')

        for column in range(self.width_in_fields):
            self.columnconfigure(column, weight=1, uniform='a')

        for row, columns in enumerate(input_data):
            for column, color in enumerate(columns):
                border_width = 1

                frame = ctk.CTkFrame(self, border_width=border_width, border_color='#000')
                label = ctk.CTkLabel(frame, text='', fg_color=Settings.colors[color])
                label.pack(expand=True, fill='both')

                frame.grid(row=row, column=column, sticky='nswe', padx=border_width, pady=border_width)


# data = [[0, 0, 0, 0, 0, 0, 4, 0, 3, 0, 4, 0], [0, 0, 0, 0, 0, 0, 0, 4, 3, 4, 0, 0], [0, 0, 0, 0, 0, 0, 3, 3, 4, 3, 3, 0], [0, 0, 0, 0, 0, 0, 0, 4, 3, 4, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 3, 0, 4, 0], [4, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0], [0, 4, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0], [3, 3, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0], [0, 4, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# window = ctk.CTk()
# window.geometry('200x200')
# DisplayGrid(window, data).place(x=0, y=0, relwidth=1, relheight=1)

# window.mainloop()
