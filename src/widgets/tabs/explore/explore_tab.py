import customtkinter as ctk

from src.widgets.tabs.explore.explore_content import ExploreContent


class ExploreTab(ctk.CTkFrame):
    def __init__(self, master, tasks_data):
        super().__init__(master)

        self.configure(fg_color='blue')

        self.content = ExploreContent(self)
        self.content.place(x=0, y=0, anchor='nw', relwidth=1, relheight=1)




