import customtkinter as ctk
import tkinter as tk

from widgets.menu import Menu
from src.widgets.tabs.home.home_tab import HomeTab
from src.widgets.tabs.explore.explore_tab import ExploreTab
from src.widgets.tabs.game.game_tab import GameTab
from src.widgets.display_grid import DisplayGrid


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        from tasks.tasks_data import TasksData
        self.tasks_data = TasksData()

        # window configuration
        self.title('ARC App')
        self.geometry('1000x800')

        # Tabs
        self.homeTab = HomeTab(self)
        self.exploreTab = ExploreTab(self, self.tasks_data)
        self.gameTab = GameTab(self)

        self.current_tab = self.homeTab
        self.set_tab(self.homeTab)
        # Menu
        self.menu = Menu(self,
                         lambda: self.set_tab(self.homeTab),
                         lambda: self.set_tab(self.exploreTab),
                         lambda: self.set_tab(self.gameTab)
                         )
        self.line = ctk.CTkFrame(self, fg_color='white')
        self.line.place(relwidth=1, relheight=0.001, relx=0, rely=0.1, anchor='nw')

        # Menu Bar
        self.menu_bar = tk.Menu(self)
        self.configure(menu=self.menu_bar)

        self.navigation_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.navigation_menu.add_command(label='Home', command=lambda: self.set_tab(self.homeTab))
        self.navigation_menu.add_command(label='Explore', command=lambda: self.set_tab(self.exploreTab))
        self.navigation_menu.add_command(label='Game', command=lambda: self.set_tab(self.gameTab))

        self.menu_bar.add_cascade(menu=self.navigation_menu, label='Navigation')

        # run
        self.mainloop()

    def set_tab(self, tab):
        if self.current_tab:
            self.current_tab.place_forget()

        self.current_tab = tab
        self.current_tab.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
