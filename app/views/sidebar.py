import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=220)

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text="Categorias",
            font=("",16,"bold")
        ).pack(
            pady=(15,10)
        )

        categorias = [

            "Todos",

            "Hat",
            "Face",
            "Hair",
            "Back",
            "Front",
            "Shoulder",
            "Waist",

            "Shirt",
            "Pants",

            "Animation"
        ]

        for categoria in categorias:

            ctk.CTkButton(
                self,
                text=categoria
            ).pack(
                fill="x",
                padx=10,
                pady=3
            )
