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
        [mission["name"], mission["difficulty"], mission["completed"]]
        for mission in data["missions"]
    ]
    print(tabulate(table, headers=["Mission", "Difficulty", "Completion Date"], tablefmt="grid"))


# Static Bar Chart
def plot_difficulty_distribution(data):
    difficulties = [mission["difficulty"] for mission in data["missions"]]
    counts = Counter(difficulties)
    plt.bar(counts.keys(), counts.values(), color=["green", "orange", "red"])
    plt.title("CheckiO Missions by Difficulty")
    plt.xlabel("Difficulty")
    plt.ylabel("Number of Missions")
    plt.show()


# Interactive Pie Chart
def plot_difficulty_pie_chart(data):
    difficulties = [mission["difficulty"] for mission in data["missions"]]
    fig = px.pie(
        names=difficulties,
        title="CheckiO Missions by Difficulty"
    )
    fig.update_traces(textinfo='percent+label')
    fig.show()


def main():
    data = load_data()

    while True:
        print("\nChoose an option:")
        print("1. View Progress (Table)")
        print("2. View Progress (Bar Chart - Matplotlib)")
        print("3. View Progress (Pie Chart - Plotly)")
        print("4. Add New Mission")
        print("5. Exit")

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
            completed = input("Enter completion date (YYYY-MM-DD): ").strip()
            data["missions"].append({"name": name, "difficulty": difficulty, "completed": completed})
            save_data(data)
            print("Mission added successfully!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
