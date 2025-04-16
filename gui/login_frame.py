import customtkinter as ctk
from utils.auth import authenticate_user

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(fg_color=("#121220", "#121220"))
        
        ctk.CTkLabel(self, text="🔐 Login", font=("Segoe UI", 24, "bold"), text_color="#ffffff").pack(pady=30)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250, corner_radius=10)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250, corner_radius=10)
        self.password_entry.pack(pady=10)

        ctk.CTkButton(self, text="Login", command=self.login, width=150, corner_radius=10).pack(pady=15)
        ctk.CTkButton(self, text="Create account", command=self.app.show_register, fg_color="transparent", text_color="#00bfff", width=150).pack()

        self.message = ctk.CTkLabel(self, text="", text_color="#ff4d4d")
        self.message.pack(pady=5)

    def login(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()
        if authenticate_user(user, pw):
            self.app.current_user = user
            self.app.show_dashboard()
        else:
            self.message.configure(text="Invalid credentials")