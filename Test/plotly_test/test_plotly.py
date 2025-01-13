# Create an interactive pie chart with Plotly:

import plotly.express as px

# Test data
labels = ["easy", "medium", "hard"]
values = [5, 3, 2]

# Create a pie chart
fig = px.pie(
    names=labels,
    values=values,
    title="Plotly Test Pie Chart",
)

# Display the chart
fig.show()
