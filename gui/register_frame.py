import customtkinter as ctk
from utils.auth import register_user

class RegisterFrame(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(fg_color=("#121220", "#121220"))

        ctk.CTkLabel(self, text="📝 Register", font=("Segoe UI", 24, "bold"), text_color="#ffffff").pack(pady=30)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Choose a username", width=250, corner_radius=10)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Choose a password", show="*", width=250, corner_radius=10)
        self.password_entry.pack(pady=10)

        ctk.CTkButton(self, text="Register", command=self.register, width=150, corner_radius=10).pack(pady=15)
        ctk.CTkButton(self, text="Back to login", command=self.app.show_login, fg_color="transparent", text_color="#00bfff", width=150).pack()

        self.message = ctk.CTkLabel(self, text="", text_color="#ff4d4d")
        self.message.pack(pady=5)

    def register(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()
        if register_user(user, pw):
            self.message.configure(text="Registration successful!", text_color="green")
        else:
            self.message.configure(text="User already exists")
