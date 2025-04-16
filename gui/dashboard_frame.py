import customtkinter as ctk
from datetime import datetime, timedelta
import json
import os

DATA_FILE = "data/tasks.json"

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, app, username):
        super().__init__(master)
        self.app = app
        self.username = username
        self.tasks = self.load_tasks()

        self.configure(fg_color="#121220")

        # Header
        header = ctk.CTkFrame(self, fg_color="#1f1f3a")
        header.pack(fill="x", pady=10)

        ctk.CTkLabel(header, text=f"Welcome, {username}", font=("Segoe UI", 18, "bold"), text_color="white").pack(side="left", padx=20, pady=10)
        ctk.CTkButton(header, text="Logout", command=self.logout, width=80, corner_radius=10).pack(side="right", padx=20)

        # Container principal com layout horizontal (flexbox-style)
        main_content = ctk.CTkFrame(self, fg_color="#121220")
        main_content.pack(pady=10, padx=20, fill="both", expand=True)

        # Esquerda: Upcoming Days
        left_section = ctk.CTkFrame(main_content, fg_color="#2c2c4a", corner_radius=12)
        left_section.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(left_section, text="Upcoming 5 Days", font=("Segoe UI", 16, "bold"), text_color="white").pack(pady=10)

        today = datetime.now()
        for i in range(5):
            day = today + timedelta(days=i)
            day_str = day.strftime("%d/%m/%Y")
            task_count = len(self.tasks.get(day_str, []))

            day_frame = ctk.CTkFrame(left_section, fg_color="#3a3a5a", corner_radius=12)
            day_frame.pack(padx=10, pady=5, fill="x")

            ctk.CTkLabel(day_frame, text=f"{day.strftime('%A')} - {day_str}", font=("Segoe UI", 12), text_color="white").pack(pady=5)
            indicator_text = f"{task_count} task(s)" if task_count > 0 else "No tasks"
            indicator_color = "#28a745" if task_count > 0 else "#dc3545"
            ctk.CTkLabel(day_frame, text=indicator_text, font=("Segoe UI", 10), text_color=indicator_color).pack(pady=5)

        # Direita: Adicionar tarefas
        right_section = ctk.CTkFrame(main_content, fg_color="#2c2c4a", corner_radius=12)
        right_section.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(right_section, text="Add New Task", font=("Segoe UI", 16, "bold"), text_color="white").pack(pady=10)

        self.title_entry = ctk.CTkEntry(right_section, placeholder_text="Task Title", width=300, corner_radius=10)
        self.title_entry.pack(pady=5)
        self.desc_entry = ctk.CTkEntry(right_section, placeholder_text="Description", width=300, corner_radius=10)
        self.desc_entry.pack(pady=5)
        self.date_entry = ctk.CTkEntry(right_section, placeholder_text="DD/MM/YYYY", width=300, corner_radius=10)
        self.date_entry.pack(pady=5)
        self.save_btn = ctk.CTkButton(right_section, text="Save Task", command=self.save_task, width=150, corner_radius=10)
        self.save_btn.pack(pady=10)

        # Parte inferior: Calendário
        self.calendar_frame = ctk.CTkFrame(self, fg_color="#2c2c4a", corner_radius=12)
        self.calendar_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.calendar_frame, text="Calendar", font=("Segoe UI", 16, "bold"), text_color="white").pack(pady=10)

    def open_add_task(self):
        self.title_entry.pack(pady=5)
        self.desc_entry.pack(pady=5)
        self.date_entry.pack(pady=5)
        self.save_btn.pack(pady=10)

    def save_task(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        date = self.date_entry.get()
        if date not in self.tasks:
            self.tasks[date] = []
        self.tasks[date].append({"title": title, "description": desc})
        self.save_tasks()
        self.app.show_dashboard()

    def logout(self):
        self.app.current_user = None
        self.app.show_login()

    def load_tasks(self):
        if not os.path.exists(DATA_FILE):
            return {}
        with open(DATA_FILE, "r") as f:
            all_tasks = json.load(f)
        return all_tasks.get(self.username, {})

    def save_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                all_tasks = json.load(f)
        else:
            all_tasks = {}
        all_tasks[self.username] = self.tasks
        with open(DATA_FILE, "w") as f:
            json.dump(all_tasks, f, indent=4)
