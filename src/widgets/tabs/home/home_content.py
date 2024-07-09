import customtkinter as ctk
import math

from src.settings import Settings

from src.widgets.multiline_text import MultilineText


class HomeContent(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color='#000')

        self.rows = (0, 1, 2, 3, 4)
        self.columns = (0, 1)

        self.width = self.winfo_width() / (2 * len(self.columns))

        self.columnconfigure(self.columns, weight=1, uniform='a')

        self.title_frame = ctk.CTkFrame(self, bg_color='black')
        self.title = ctk.CTkLabel(self.title_frame, text='ARC', font=Settings.large_title_format, bg_color='black')
        self.title.pack(expand=True, fill='both')
        self.title_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky='nswe')

        self.frames = [self.new_frame('ARC PRIZE',
                                      "ARC Prize is a $1,000,000+ public competition to beat and open source a solution to the ARC-AGI benchmark.\n\nHosted by Mike Knoop (Co-founder, Zapier) and François Chollet (Creator of ARC-AGI, Keras).",
                                      '#e53aa3',
                                      ),

                       self.new_frame('ARC-AGI',
                                      "Most AI benchmarks measure skill. But skill is not intelligence. General intelligence is the ability to efficiently acquire new skills. Chollet's unbeaten 2019 Abstraction and Reasoning Corpus for Artificial General Intelligence (ARC-AGI) is the only formal benchmark of AGI.\n\nIt's easy for humans, but hard for AI",
                                      '#1f93ff'
                                      ),

                       self.new_frame('AGI',
                                      "Progress toward artificial general intelligence (AGI) has stalled. LLMs are trained on unimaginably vast amounts of data, yet they remain unable to adapt to simple problems they haven't been trained on, or make novel inventions, no matter how basic.\n\nStrong market incentives have pushed frontier AI research to go closed source. Research attention and resources are being pulled toward a dead end. You can change that.",
                                      "#e53aa3"
                                      ),

                       self.new_frame('DEFINING AGI',
                                      "Consensus but\nwrong:\nAGI is a system that can automate the majority of economically valuable work.\n\nCorrect:\nAGI is a system that can efficiently acquire new skills and solve open-ended problems.\n\nDefinitions are important. We turn them into benchmarks to measure progress toward AGI.\n\nWithout AGI, we will never have systems that can invent and discover alongside humans.",
                                      '#1f93ff'
                                      ),

                       self.new_frame('COOL STUFF HERE',
                                      "- Explore the world of ARC in the Explore Tab\n\n- Test your ARC solving skills in the Game Tab\n\n- But to be honest, there is nothing special ",
                                      '#e53aa3'
                                      ),
                       self.new_frame('Bugs?',
                                      "Did you find a bug? No you didn't. There are no bugs. That's why there is no report function. \nOk. I have to say this isn't public, so a report function wouldn't use anything ",
                                      '#1f93ff'
                                      )


                       ]

        for index, item in enumerate(self.frames):

            if index % 2 == 0:
                column = 0
            else:
                column = 1

            row = math.floor(float(index) / 2) + 1

            item.grid(row=row, column=column, sticky='nswe')

    def new_frame(self, title, body, color):
        frame = ctk.CTkFrame(self, fg_color='black', corner_radius=0, border_width=1, border_color='#333')

        title = ctk.CTkLabel(frame, text=title, text_color=color, font=Settings.small_title_format)
        body = MultilineText(frame, text=body)

        title.pack(padx=10, pady=12, fill='both')
        body.pack(padx=10, pady=15, fill='both')

        return frame
