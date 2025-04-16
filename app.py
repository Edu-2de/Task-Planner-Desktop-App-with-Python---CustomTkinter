import customtkinter as ctk
from datetime import datetime

# Sistema de Login
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "password":
        app_login.destroy()
        create_task_ui()
    else:
        label_error.config(text="Invalid username or password", text_color="red")

# Função de registro
def register():
    app_register = ctk.CTk()
    app_register.title("Register")
    app_register.geometry("400x400")
    app_register.config(bg="gray15")

    label_username = ctk.CTkLabel(app_register, text="Username", font=("Arial", 14), text_color="white")
    label_username.pack(pady=10)
    entry_username_reg = ctk.CTkEntry(app_register, placeholder_text="Enter username", font=("Arial", 14))
    entry_username_reg.pack(pady=5)

    label_password = ctk.CTkLabel(app_register, text="Password", font=("Arial", 14), text_color="white")
    label_password.pack(pady=10)
    entry_password_reg = ctk.CTkEntry(app_register, placeholder_text="Enter password", font=("Arial", 14), show="*")
    entry_password_reg.pack(pady=5)

    label_confirm_password = ctk.CTkLabel(app_register, text="Confirm Password", font=("Arial", 14), text_color="white")
    label_confirm_password.pack(pady=10)
    entry_confirm_password = ctk.CTkEntry(app_register, placeholder_text="Confirm password", font=("Arial", 14), show="*")
    entry_confirm_password.pack(pady=5)

    def register_user():
        username = entry_username_reg.get()
        password = entry_password_reg.get()
        confirm_password = entry_confirm_password.get()

        if password == confirm_password:
            # Aqui você pode adicionar o código para salvar o novo usuário (em banco de dados, por exemplo)
            app_register.destroy()
            label_error.config(text="Registration successful", text_color="green")
            login()  # Após o registro, já loga automaticamente
        else:
            label_error.config(text="Passwords do not match", text_color="red")

    button_register = ctk.CTkButton(app_register, text="Register", command=register_user, font=("Arial", 14), width=200, fg_color="#4CAF50", hover_color="#45a049")
    button_register.pack(pady=10)

    app_register.mainloop()

# Tela de Login
def show_login():
    global app_login, entry_username, entry_password, label_error
    app_login = ctk.CTk()
    app_login.title("Login")
    app_login.geometry("400x300")
    app_login.config(bg="gray15")

    label_username = ctk.CTkLabel(app_login, text="Username", font=("Arial", 14), text_color="white")
    label_username.pack(pady=10)
    entry_username = ctk.CTkEntry(app_login, placeholder_text="Enter username", font=("Arial", 14))
    entry_username.pack(pady=5)

    label_password = ctk.CTkLabel(app_login, text="Password", font=("Arial", 14), text_color="white")
    label_password.pack(pady=10)
    entry_password = ctk.CTkEntry(app_login, placeholder_text="Enter password", font=("Arial", 14), show="*")
    entry_password.pack(pady=5)

    label_error = ctk.CTkLabel(app_login, text="", font=("Arial", 12))
    label_error.pack(pady=5)

    button_login = ctk.CTkButton(app_login, text="Login", command=login, font=("Arial", 14), width=200, fg_color="#4CAF50", hover_color="#45a049")
    button_login.pack(pady=10)

    button_register = ctk.CTkButton(app_login, text="Create Account", command=register, font=("Arial", 14), width=200, fg_color="#00BFFF", hover_color="#009ACD")
    button_register.pack(pady=10)

    app_login.mainloop()

# Função para criar a UI de tarefas após login
def create_task_ui():
    app_task = ctk.CTk()
    app_task.title("Task Planner")
    app_task.geometry("400x500")
    app_task.config(bg="gray15")

    task_list = []

    def add_task():
        title = entry_title.get()
        description = entry_description.get()
        date = entry_date.get()
        if title and description and date:
            task_list.append({"title": title, "description": description, "date": date})
            update_task_list()

    def update_task_list():
        for widget in frame_tasks.winfo_children():
            widget.destroy()

        for task in task_list:
            task_info = f"{task['title']} - {task['date']}\n{task['description']}"
            label_task = ctk.CTkLabel(frame_tasks, text=task_info, font=("Arial", 12), text_color="white", anchor="w")
            label_task.pack(pady=5, padx=10, fill="x")

    label = ctk.CTkLabel(app_task, text="Task Planner", font=("Arial", 20), text_color="white")
    label.pack(pady=20)

    label_title = ctk.CTkLabel(app_task, text="Title", font=("Arial", 14), text_color="white")
    label_title.pack(pady=5)
    entry_title = ctk.CTkEntry(app_task, placeholder_text="Enter task title", font=("Arial", 14), width=300)
    entry_title.pack(pady=5)

    label_description = ctk.CTkLabel(app_task, text="Description", font=("Arial", 14), text_color="white")
    label_description.pack(pady=5)
    entry_description = ctk.CTkEntry(app_task, placeholder_text="Enter task description", font=("Arial", 14), width=300)
    entry_description.pack(pady=5)

    label_date = ctk.CTkLabel(app_task, text="Due Date (YYYY-MM-DD)", font=("Arial", 14), text_color="white")
    label_date.pack(pady=5)
    entry_date = ctk.CTkEntry(app_task, placeholder_text="Enter task date", font=("Arial", 14), width=300)
    entry_date.pack(pady=5)

    button_add_task = ctk.CTkButton(app_task, text="Add Task", command=add_task, font=("Arial", 14), fg_color="#4CAF50", hover_color="#45a049", width=300)
    button_add_task.pack(pady=10)

    frame_tasks = ctk.CTkFrame(app_task, bg_color="gray20")
    frame_tasks.pack(pady=10, fill="both", expand=True)

    app_task.mainloop()

# Inicia a tela de login
show_login()
