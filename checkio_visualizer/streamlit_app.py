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
        fig = px.pie(
            df,
            names="difficulty",
            title="CheckiO Missions by Difficulty",
            color="difficulty",
            color_discrete_map={"easy": "green", "medium": "orange", "hard": "red"}
        )
        st.plotly_chart(fig)

    # Add New Mission
    st.write("## Add New Mission")
    with st.form("Add Mission"):
        name = st.text_input("Mission Name")
        difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
        category = st.text_input("Category")
        completed = st.date_input("Completion Date").strftime("%Y-%m-%d")
        time_taken = st.number_input("Time Taken (in minutes)", min_value=1)
        submitted = st.form_submit_button("Add Mission")
        if submitted:
            data["missions"].append({
                "name": name,
                "difficulty": difficulty,
                "category": category,
                "completed": completed,
                "time_taken": time_taken
            })
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
            st.success("Mission added successfully!")

if __name__ == "__main__":
    main()
