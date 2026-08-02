import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        self.label = ctk.CTkLabel(
            self,
            text="Usuário"
        )

        self.label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Nome ou ID do usuário"
        )

        self.entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5
        )

        self.button = ctk.CTkButton(
            self,
            text="Buscar"
        )

        self.button.grid(
            row=0,
            column=2,
            padx=10
        )
