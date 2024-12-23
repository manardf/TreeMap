import plotly.express as px
import pandas as pd

# Define the data structure
data = {
    "Main Source": [
        "Data Sources for Remote Working Analysis"] * 9,
    "Data Source": [
        "Microsoft Teams Usage", "Email Usage", 
        "Copilot Activity", "One Drive Usage", 
        "SharePoint Usage", "Yammer Usage", 
        "Forms Usage", "VPN Access", 
        "LogIn Duration to Device"
    ],
    "Description": [
        "Usage statistics of Microsoft Teams, including meetings and chats",
        "Volume and frequency of employee email activity",
        "Copilot utilization metrics for task assistance and automation",
        "Data on files uploaded, downloaded, and shared via One Drive",
        "Usage of SharePoint for document collaboration and team sites",
        "Employee engagement on Yammer platform",
        "Form submissions and activities within Microsoft Forms",
        "VPN login activity and duration",
        "Total time spent logged into devices by employees"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define custom colors
custom_colors = ["#2d13ea", "#ff7800", "#50d88d", "#40e2d2", "#ffc000", "#1d1d1d"]

# Create a Treemap chart
fig = px.treemap(
    df, 
    path=["Main Source", "Data Source"], 
    values=None,  # Values are not necessary as we are just showing structure
    hover_name="Description",  # Shows description on hover
    title="Data Sources for Remote Working Analysis",
    color_discrete_sequence=custom_colors
)

# Update layout for a clearer display
fig.update_layout(margin=dict(t=40, l=0, r=0, b=0))

# Save the chart as an HTML file
fig.write_html("treemap_chart.html")

# Show the chart in the browser (optional)
fig.show()