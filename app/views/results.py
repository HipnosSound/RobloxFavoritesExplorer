import customtkinter as ctk


class ResultsView(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(master)

        self.show_placeholder()

    def clear(self):
        """Remove todos os widgets da área de resultados."""

        for widget in self.winfo_children():
            widget.destroy()

    def show_placeholder(self):
        """Mostra uma mensagem enquanto não há resultados."""

        self.clear()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(expand=True, fill="both", pady=100)

        ctk.CTkLabel(
            container,
            text="🔎",
            font=("Arial", 60)
        ).pack(pady=(0, 20))

        ctk.CTkLabel(
            container,
            text="Pesquise um usuário para começar.",
            font=("Arial", 22, "bold")
        ).pack()

        ctk.CTkLabel(
            container,
            text="Os favoritos públicos do Marketplace aparecerão aqui.",
            font=("Arial", 14)
        ).pack(pady=10)

    def show_items(self, items):
        """
        No momento apenas limpa a tela.
        Depois vamos preencher com FavoriteCard.
        """

        self.clear()

        # Em breve:
        #
        # for item in items:
        #     FavoriteCard(...)
