"""
Parse all the collected HTML files
Author: Kenneth
Date: CS299 2024
"""

from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt


# Load the HTML file
# videos_df = pd.DataFrame("videos" = [])
young_videos_df = pd.DataFrame()
mid_videos_df = pd.DataFrame()
old_videos_df = pd.DataFrame()
for path in os.listdir("./parsed_pages"):
    if path.endswith(".html"):
        file_path = os.path.join("./parsed_pages", path)
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the element by ID and class

        # In this case, we're looking for both id and class attributes.

        # If you expect multiple items
        items = soup.find_all("ytk-compact-video-renderer")
        items += soup.find_all("ytk-compact-playlist-renderer")

        # Print out the content of each found element
        video_list = []
        for item in items:
            video_info = item.find_all("a")
            video_runtime = item.find(
                class_="overlay style-scope ytk-compact-video-renderer"
            )
            if video_runtime == None:
                video_runtime = item.find(
                    class_="overlay style-scope ytk-compact-playlist-renderer"
                )
            video_list.append(
                [video_info[0]["title"], video_info[0]["href"], video_runtime.text]
            )
        # store in respected age df
        if path[0] == "0":
            young_videos_df = pd.concat(
                [young_videos_df, pd.DataFrame(video_list)], ignore_index=True
            )
        elif path[0] == "1":
            mid_videos_df = pd.concat(
                [mid_videos_df, pd.DataFrame(video_list)], ignore_index=True
            )
        elif path[0] == "2":
            old_videos_df = pd.concat(
                [old_videos_df, pd.DataFrame(video_list)], ignore_index=True
            )
videos_df = pd.concat(
    [young_videos_df, mid_videos_df, old_videos_df], axis=1, ignore_index=True
)
videos_df.to_csv("videos.csv")
