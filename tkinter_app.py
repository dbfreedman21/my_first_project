import tkinter as tk
from tkinter import ttk
import json

# Load data
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"missions": []}

data = load_data()

# Tkinter App
def main():
    root = tk.Tk()
    root.title("CheckiO Progress Tracker")

    # Frame for Table
    frame = ttk.Frame(root)
    frame.pack(pady=20)

    tree = ttk.Treeview(frame, columns=["name", "difficulty", "category", "completed", "time_taken"], show="headings")
    for col in ["name", "difficulty", "category", "completed", "time_taken"]:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=120)
    tree.pack()

    for mission in data["missions"]:
        tree.insert("", tk.END, values=(
            mission["name"], mission["difficulty"], mission["category"], mission["completed"], f"{mission['time_taken']} min"
        ))

    # Form to Add New Mission
    def add_mission():
        mission = {
            "name": name_var.get(),
            "difficulty": difficulty_var.get(),
            "category": category_var.get(),
            "completed": completed_var.get(),
            "time_taken": time_var.get()
        }
        data["missions"].append(mission)
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        tree.insert("", tk.END, values=(
            mission["name"], mission["difficulty"], mission["category"], mission["completed"], f"{mission['time_taken']} min"
        ))
        success_label.config(text="Mission added successfully!")

    # Input Fields
    name_var = tk.StringVar()
    difficulty_var = tk.StringVar()
    category_var = tk.StringVar()
    completed_var = tk.StringVar()
    time_var = tk.IntVar()

    tk.Label(root, text="Name:").pack()
    tk.Entry(root, textvariable=name_var).pack()
    tk.Label(root, text="Difficulty:").pack()
    tk.Entry(root, textvariable=difficulty_var).pack()
    tk.Label(root, text="Category:").pack()
    tk.Entry(root, textvariable=category_var).pack()
    tk.Label(root, text="Completed:").pack()
    tk.Entry(root, textvariable=completed_var).pack()
    tk.Label(root, text="Time Taken (min):").pack()
    tk.Entry(root, textvariable=time_var).pack()

    tk.Button(root, text="Add Mission", command=add_mission).pack()
    success_label = tk.Label(root, text="")
    success_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
