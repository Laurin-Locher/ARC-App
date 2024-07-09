import customtkinter as ctk

from src.widgets.display_grid import DisplayGrid
from src.settings import Settings


def create_preview(name, preview_data):
    frame = ctk.CTkFrame(window)
    preview = DisplayGrid(frame, preview_data)
    title = ctk.CTkLabel(frame, text=name, font=Settings.body_format)

    # Actions
    actions_frame = ctk.CTkFrame(frame)
    actions_frame.columnconfigure((0, 1, 2), weight=1)

    open_task = ctk.CTkButton(actions_frame, text='Open', command=lambda: print('Open'))
    try_task = ctk.CTkButton(actions_frame, text='try', command=lambda: print('try'))
    copy_task = ctk.CTkButton(actions_frame, text='copy', command=lambda: print('copy'))

    open_task.grid(row=0, column=0, sticky='nswe', padx=2)
    try_task.grid(row=0, column=0, sticky='nswe', padx=2)
    copy_task.grid(row=0, column=0, sticky='nswe', padx=2)

    preview.pack(expand=True, fill='x', padx=20, pady=20)
    title.pack(padx=20)
    # actions_frame.pack(expand=True, fill='both')

    window.bind('<Configure>', lambda event: preview.configure(height=event.width))

    return frame


window = ctk.CTk()
window.geometry('300x500')

data = [[0, 0, 0, 0, 0, 0, 4, 0, 3, 0, 4, 0], [0, 0, 0, 0, 0, 0, 0, 4, 3, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 3, 4, 3, 3, 0], [0, 0, 0, 0, 0, 0, 0, 4, 3, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 3, 0, 4, 0], [4, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0], [3, 3, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
create_preview('N01 #1 TestV1', data).pack()

window.mainloop()