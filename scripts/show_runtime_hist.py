"""
Visualize screen time for all three age groups using histograms
Author: Kenneth
Class: CS299 2024
"""

import plotly.graph_objects as go
import numpy as np
import pandas as pd


def time_to_hours(time_str):
    # Convert time into hours
    try:
        h, m, s = map(int, time_str.split(":"))
    except ValueError:
        h = 0
        m, s = map(int, time_str.split(":"))
    return h + m / 60 + s / 3600


videos_df = pd.read_csv("videos.csv")

# Create a figure
fig = go.Figure()

name_list = ["Preschool(0-4)", "Younger(5-8)", "Older(9-12)"]
name_idx = 0
for age_index in range(2, len(videos_df.columns), 3):
    time_stamp_list = list(videos_df[str(age_index)])
    time_stamp_list = [  # prune out playlists
        time_to_hours(item)
        for item in time_stamp_list
        if type(item) == str and "videos" not in item
    ]
    # Add three histogram traces with 30 bins each

    fig.add_trace(
        go.Histogram(
            x=time_stamp_list,
            nbinsx=60,
            name=name_list[name_idx],
            hovertemplate="Video Length: %{x} Hours<br>Count: %{y} Videos",
        )
    )
    name_idx += 1

# Update layout for better readability
fig.update_layout(
    title="Length of Recommend Videos per Age",
    xaxis_title="Length(Hours)",
    yaxis_title="Frequency",
    barmode="overlay",  # Overlays the bars for better comparison
)
fig.update_xaxes(tickvals=np.arange(0, 12, 0.5), ticktext=np.arange(0, 12, 0.5))


# Show the figure
fig.show()
fig.write_html("run_time.html")
