import customtkinter as ctk
from src.settings import Settings


class Menu(ctk.CTkFrame):
    def __init__(self, master, set_home, set_explore, set_game):
        super().__init__(master)

        self.set_home = set_home
        self.set_explore = set_explore
        self.set_game = set_game

        # Frame configuration
        self.configure(fg_color='#000')
        self.configure(corner_radius=0)

        # self.configure(border_width=2, border_color='white')

        # Create Widgets
        self.create_widgets()

        # Create Layout
        self.create_layout()

        # Place
        self.place(relwidth=1, relheight=0.1, relx=0, rely=0, anchor='nw')

    def create_logo(self):
        frame = ctk.CTkFrame(self)
        frame.configure(height=100, width=500)
        # frame.bind('<Configure>',
        #            lambda event: frame.configure(width=frame.winfo_height() * 2.5))

        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        frame.rowconfigure((0, 1), weight=1, uniform='a')

        # ARC
        a = ctk.CTkLabel(frame, text='A', font=Settings.logo_format)
        r = ctk.CTkLabel(frame, text='R', font=Settings.logo_format)
        c = ctk.CTkLabel(frame, text='C', font=Settings.logo_format)

        square_1 = ctk.CTkLabel(frame, text='', fg_color='#e53aa3')
        square_2 = ctk.CTkLabel(frame, text='', fg_color='#ffdc00')

        # PRIZE
        p = ctk.CTkLabel(frame, text='P', font=Settings.logo_format)
        r2 = ctk.CTkLabel(frame, text='R', font=Settings.logo_format)
        i = ctk.CTkLabel(frame, text='I', font=Settings.logo_format)
        z = ctk.CTkLabel(frame, text='Z', font=Settings.logo_format)
        e = ctk.CTkLabel(frame, text='E', font=Settings.logo_format)

        a.grid(row=0, column=0, sticky='nswe')
        r.grid(row=0, column=1, sticky='nswe')
        c.grid(row=0, column=2, sticky='nswe')

        square_1.grid(row=0, column=3, sticky='nswe', padx=10, pady=10)
        square_2.grid(row=0, column=4, sticky='nswe', padx=10, pady=10)

        p.grid(row=1, column=0, sticky='nswe')
        r2.grid(row=1, column=1, sticky='nswe')
        i.grid(row=1, column=2, sticky='nswe')
        z.grid(row=1, column=3, sticky='nswe')
        e.grid(row=1, column=4, sticky='nswe')

        return frame

    def create_widgets(self):
        def create_tab(name, command):
            return ctk.CTkButton(self, text=name, text_color='#fff',
                                 fg_color='transparent',
                                 hover_color='#222',
                                 font=Settings.tab_buttons_format,
                                 command=command)

        # self.logo = ctk.CTkLabel(self, text='ARC', text_color='#fff', font=Settings.logo_format)
        self.logo = self.create_logo()

        self.home_tab_button = create_tab('Home', self.set_home)
        self.explore_tab_button = create_tab('Explore', self.set_explore)
        self.game_tab_button = create_tab('Game', self.set_game)

    def create_layout(self):
        self.logo.pack(side='left', padx=20)

        def pack_tab(tab):
            tab.pack(side='right', padx=10, pady=10, ipadx=5, ipady=5)

        pack_tab(self.game_tab_button)
        pack_tab(self.explore_tab_button)
        pack_tab(self.home_tab_button)
