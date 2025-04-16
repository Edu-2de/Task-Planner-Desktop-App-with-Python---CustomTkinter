import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("🌟 Task Planner")
app.geometry("500x600")

# Imagem de fundo (opcional)
try:
    bg_image = Image.open("background.jpg")  # sua imagem de fundo
    bg_image = bg_image.resize((500, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass

title_label = ctk.CTkLabel(app, text="✨ Task Planner", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

frame_form = ctk.CTkFrame(app, corner_radius=12, fg_color="#1e1e1e")
frame_form.pack(padx=20, pady=10, fill="x")

entry_title = ctk.CTkEntry(frame_form, placeholder_text="Task Title", font=("Arial", 14))
entry_title.pack(pady=10, padx=10, fill="x")

entry_description = ctk.CTkEntry(frame_form, placeholder_text="Description", font=("Arial", 14))
entry_description.pack(pady=10, padx=10, fill="x")

entry_date = ctk.CTkEntry(frame_form, placeholder_text="Due Date (YYYY-MM-DD)", font=("Arial", 14))
entry_date.pack(pady=10, padx=10, fill="x")

task_frame = ctk.CTkFrame(app, corner_radius=12, fg_color="#2e2e2e")
task_frame.pack(padx=20, pady=10, fill="both", expand=True)

task_list = []

def add_task():
    title = entry_title.get()
    desc = entry_description.get()
    date = entry_date.get()
    if title and desc and date:
        task_data = {"title": title, "description": desc, "date": date}
        task_list.append(task_data)
        update_tasks()

def update_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for task in task_list:
        card = ctk.CTkFrame(task_frame, corner_radius=10, fg_color="#3c3c3c")
        card.pack(pady=5, padx=10, fill="x")

        lbl_title = ctk.CTkLabel(card, text=f"📌 {task['title']}", font=("Arial", 16, "bold"))
        lbl_title.pack(anchor="w", padx=10, pady=(5, 0))

        lbl_desc = ctk.CTkLabel(card, text=f"{task['description']}", font=("Arial", 12))
        lbl_desc.pack(anchor="w", padx=10)

        lbl_date = ctk.CTkLabel(card, text=f"🗓️ Due: {task['date']}", font=("Arial", 12, "italic"))
        lbl_date.pack(anchor="w", padx=10, pady=(0, 5))

btn_add = ctk.CTkButton(app, text="➕ Add Task", command=add_task, font=("Arial", 14), fg_color="#00b894", hover_color="#019870")
btn_add.pack(pady=15)

app.mainloop()
