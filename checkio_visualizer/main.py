# The main application logic.

from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import Counter
import plotly.express as px
import json


# Load and Save Data
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"missions": []}


def save_data(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# Display Data as Table
def display_table(data):
    table = [
        [mission["name"], mission["difficulty"], mission["category"], mission["completed"], f"{mission['time_taken']} min"]
        for mission in data["missions"]
    ]
    print(tabulate(table, headers=["Mission", "Difficulty", "Category", "Completion Date", "Time Taken"], tablefmt="grid"))


# Static Bar Chart
def plot_difficulty_distribution(data):
    difficulties = [mission["difficulty"] for mission in data["missions"]]
    counts = Counter(difficulties)

    colors = {"easy": "green", "medium": "orange", "hard": "red"}
    bar_colors = [colors[d] for d in counts.keys()]

    plt.bar(counts.keys(), counts.values(), color=bar_colors)
    plt.title("CheckiO Missions by Difficulty", fontsize=14)
    plt.xlabel("Difficulty", fontsize=12)
    plt.ylabel("Number of Missions", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Interactive Pie Chart
def plot_difficulty_pie_chart(data):
    difficulties = [mission["difficulty"] for mission in data["missions"]]
    fig = px.pie(
        names=difficulties,
        title="CheckiO Missions by Difficulty",
        color=difficulties,
        color_discrete_map={"easy": "green", "medium": "orange", "hard": "red"}
    )
    fig.update_traces(textinfo='percent+label', hoverinfo='label+percent+value')
    fig.show()


# Summary of Progress
def display_summary(data):
    total_missions = len(data["missions"])
    difficulty_counts = Counter(m["difficulty"] for m in data["missions"])
    
    print("\nProgress Summary:")
    print(f"Total Missions Completed: {total_missions}")
    for difficulty, count in difficulty_counts.items():
        percentage = (count / total_missions) * 100
        print(f"- {difficulty.capitalize()}: {count} ({percentage:.1f}%)")


def main():
    data = load_data()

    while True:
        print("\nChoose an option:")
        print("1. View Progress (Table)")
        print("2. View Progress (Bar Chart - Matplotlib)")
        print("3. View Progress (Pie Chart - Plotly)")
        print("4. Add New Mission")
        print("5. View Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_table(data)
        elif choice == "2":
            plot_difficulty_distribution(data)
        elif choice == "3":
            plot_difficulty_pie_chart(data)
        elif choice == "4":
            name = input("Enter mission name: ").strip()
            difficulty = input("Enter difficulty (easy/medium/hard): ").strip().lower()
            category = input("Enter category (e.g., math, strings, algorithms): ").strip().lower()
            completed = input("Enter completion date (YYYY-MM-DD): ").strip()
            time_taken = int(input("Enter time taken to complete (in minutes): ").strip())
            data["missions"].append({
                "name": name,
                "difficulty": difficulty,
                "category": category,
                "completed": completed,
                "time_taken": time_taken
            })
            save_data(data)
            print("Mission added successfully!")
        elif choice == "5":
            display_summary(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import Counter
import plotly.express as px
import json


# Load and Save Data
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"missions": []}


def save_data(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# Display Data as Table
def display_table(data):
    table = [
        [mission["name"], mission["difficulty"], mission["category"], mission["completed"], f"{mission['time_taken']} min"]
        for mission in data["missions"]
    ]
    print(tabulate(table, headers=["Mission", "Difficulty", "Category", "Completion Date", "Time Taken"], tablefmt="grid"))


# Static Bar Chart
def plot_difficulty_distribution(data):
    difficulties = [mission["difficulty"] for mission in data["missions"]]
    counts = Counter(difficulties)

    colors = {"easy": "green", "medium": "orange", "hard": "red"}
    bar_colors = [colors[d] for d in counts.keys()]

    plt.bar(counts.keys(), counts.values(), color=bar_colors)
    plt.title("CheckiO Missions by Difficulty", fontsize=14)
    plt.xlabel("Difficulty", fontsize=12)
    plt.ylabel("Number of Missions", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Interactive Pie Chart
def plot_difficulty_pie_chart(data):
    difficulties = [mission["difficulty"] for mission in data["missions"]]
    fig = px.pie(
        names=difficulties,
        title="CheckiO Missions by Difficulty",
        color=difficulties,
        color_discrete_map={"easy": "green", "medium": "orange", "hard": "red"}
    )
    fig.update_traces(textinfo='percent+label', hoverinfo='label+percent+value')
    fig.show()


# Summary of Progress
def display_summary(data):
    total_missions = len(data["missions"])
    difficulty_counts = Counter(m["difficulty"] for m in data["missions"])
    
    print("\nProgress Summary:")
    print(f"Total Missions Completed: {total_missions}")
    for difficulty, count in difficulty_counts.items():
        percentage = (count / total_missions) * 100
        print(f"- {difficulty.capitalize()}: {count} ({percentage:.1f}%)")


def main():
    data = load_data()

    while True:
        print("\nChoose an option:")
        print("1. View Progress (Table)")
        print("2. View Progress (Bar Chart - Matplotlib)")
        print("3. View Progress (Pie Chart - Plotly)")
        print("4. Add New Mission")
        print("5. View Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_table(data)
        elif choice == "2":
            plot_difficulty_distribution(data)
        elif choice == "3":
            plot_difficulty_pie_chart(data)
        elif choice == "4":
            name = input("Enter mission name: ").strip()
            difficulty = input("Enter difficulty (easy/medium/hard): ").strip().lower()
            category = input("Enter category (e.g., math, strings, algorithms): ").strip().lower()
            completed = input("Enter completion date (YYYY-MM-DD): ").strip()
            time_taken = int(input("Enter time taken to complete (in minutes): ").strip())
            data["missions"].append({
                "name": name,
                "difficulty": difficulty,
                "category": category,
                "completed": completed,
                "time_taken": time_taken
            })
            save_data(data)
            print("Mission added successfully!")
        elif choice == "5":
            display_summary(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
