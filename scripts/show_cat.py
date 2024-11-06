import pandas as pd
import plotly.graph_objects as go
import numpy as np

video_df = pd.read_csv("./gpt_categorized.csv")
video_df = video_df[["4", "5", "6"]]
video_df.columns = ["Preschool", "Younger", "Older"]
counts = video_df.apply(lambda x: x.value_counts(normalize=True))

fig = go.Figure()
for age_group in video_df.columns:
    fig.add_trace(
        go.Bar(
            x=counts.index,
            y=counts[age_group],
            name=age_group,
            hovertemplate="%{y:.0%} of Videos",
        )
    )

fig.update_yaxes(tickformat=".0%")
fig.update_layout(
    title="Categorized Videos for Each Age(Normalized)",
    xaxis_title="Video Category",
    yaxis_title="Percent of Total",
)
fig.show()
fig.write_html("category.html")
