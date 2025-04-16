import customtkinter as ctk
from gui.login_frame import LoginFrame
from gui.dashboard_frame import DashboardFrame
from gui.register_frame import RegisterFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Task Planner")

        # Definindo um tamanho inicial e permitindo redimensionamento
        self.geometry("1200x800")  # Tamanho inicial da janela
        self.minsize(800, 600)  # Tamanho mínimo que a janela pode ter
        self.configure(bg="#121220")  # Cor de fundo do app

        self.current_user = None

        # Inicializando as páginas
        self.login_frame = LoginFrame(self, self)
        self.register_frame = RegisterFrame(self, self)
        self.dashboard_frame = None

        self.show_login()

    def show_login(self):
        self.register_frame.pack_forget()
        if self.dashboard_frame:
            self.dashboard_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def show_register(self):
        self.login_frame.pack_forget()
        if self.dashboard_frame:
            self.dashboard_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        if self.dashboard_frame is None:
            self.dashboard_frame = DashboardFrame(self, self, self.current_user)
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.dashboard_frame.pack(fill="both", expand=True)


# Inicializando o app
if __name__ == "__main__":
    app = App()
    app.mainloop()
