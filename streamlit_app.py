import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Load data
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"missions": []}

# Save data
def save_data(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Main app
def main():
    data = load_data()
    df = pd.DataFrame(data["missions"])

    st.title("CheckiO Progress Tracker")

    # Display Data Table
    st.write("## Missions Overview")
    if not df.empty:
        st.dataframe(df)

    # Bar Chart
    st.write("## Difficulty Distribution (Bar Chart)")
    if not df.empty:
        difficulty_counts = df["difficulty"].value_counts()
        st.bar_chart(difficulty_counts)

    # Pie Chart
    st.write("## Difficulty Distribution (Pie Chart)")
    if not df.empty:
        fig = px.pie(df, names='difficulty', title='Difficulty Distribution')
        st.plotly_chart(fig)

    # Form to Add New Mission
    st.write("## Add New Mission")
    with st.form(key='add_mission_form'):
        name = st.text_input("Name")
        difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
        category = st.text_input("Category")
        completed = st.text_input("Completed")
        time_taken = st.number_input("Time Taken (min)", min_value=0)
        submit_button = st.form_submit_button(label='Add Mission')

        if submit_button:
            new_mission = {
                "name": name,
                "difficulty": difficulty,
                "category": category,
                "completed": completed,
                "time_taken": time_taken
            }
            data["missions"].append(new_mission)
            save_data(data)
            st.success("Mission added successfully!")
            st.experimental_rerun()

if __name__ == "__main__":
    main()
