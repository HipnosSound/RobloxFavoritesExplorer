import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text="Pronto."
        )

        self.label.pack(
            anchor="w",
            padx=10,
            pady=6
        )
