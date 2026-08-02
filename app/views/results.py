import customtkinter as ctk


class ResultsView(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(master)

        for i in range(8):

            card = ctk.CTkFrame(
                self,
                width=180,
                height=230
            )

            card.grid(
                row=i//4,
                column=i%4,
                padx=12,
                pady=12
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text="Miniatura",
                width=150,
                height=120
            ).pack(
                pady=(12,5)
            )

            ctk.CTkLabel(
                card,
                text="Item Exemplo"
            ).pack()

            ctk.CTkLabel(
                card,
                text="FaceAccessory"
            ).pack()

            ctk.CTkButton(
                card,
                text="Abrir"
            ).pack(
                pady=10
            )
