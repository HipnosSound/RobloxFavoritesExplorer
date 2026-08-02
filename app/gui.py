import customtkinter as ctk

from app.views.toolbar import Toolbar
from app.views.sidebar import Sidebar
from app.views.results import ResultsView
from app.views.statusbar import StatusBar

from app.settings import APP_NAME, VERSION


class App:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()

        self.window.title(f"{APP_NAME} {VERSION}")

        self.window.geometry("1280x720")

        self.window.minsize(1000, 650)

        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        self.toolbar = Toolbar(self.window)
        self.toolbar.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=10
        )

        self.sidebar = Sidebar(self.window)
        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(10,5),
            pady=5
        )

        self.results = ResultsView(self.window)
        self.results.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(5,10),
            pady=5
        )

        self.status = StatusBar(self.window)
        self.status.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=10
        )

    def run(self):

        self.window.mainloop()
