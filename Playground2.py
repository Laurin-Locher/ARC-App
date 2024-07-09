import customtkinter as ctk
from src.settings import Settings

window = ctk.CTk()
window.geometry('250x100')


def create_logo():
    def create_labels(string):
        labels = []
        for letter in string:
            label = ctk.CTkLabel(frame, text=letter, font=Settings.logo_format)
            labels.append(label)

        return labels

    final_frame = ctk.CTkFrame(window, bg_color='red')
    frame = ctk.CTkFrame(final_frame)
    frame.configure()

    # frame.bind('<Configure>',
    #            lambda event: frame.configure(width=frame.winfo_height() * 2.5))

    frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
    frame.rowconfigure((0, 1), weight=1, uniform='a')

    # ARC
    arc_labels = create_labels('ARC')

    square_1 = ctk.CTkLabel(frame, text='', fg_color='#e53aa3')
    square_2 = ctk.CTkLabel(frame, text='', fg_color='#ffdc00')

    # PRIZE
    prize_labels = create_labels('PRIZE')

    for index, label in enumerate(arc_labels):
        label.grid(row=0, column=index, sticky='nswe')

    square_1.grid(row=0, column=3, sticky='nswe', padx=10, pady=10)
    square_2.grid(row=0, column=4, sticky='nswe', padx=10, pady=10)

    for index, label in enumerate(prize_labels):
        label.grid(row=1, column=index, sticky='nswe')

    frame.pack(expand=True, fill='both')

    return final_frame


create_logo().place(x=0, y=0)

window.mainloop()
