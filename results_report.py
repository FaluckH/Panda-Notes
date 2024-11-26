import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("results.csv")

# profile = ProfileReport(df, title = "International Results")

# profile.to_file('results_report.html')

import pandas as pd

# ----------------Notes -------------------------

# df = pd.read_csv("sup_spotify_songs.csv")

# print(df["playlist_genre"].value_counts())

# print(df["playlist_genre"].mode())

# print(df["duration_ms"].median())
# print(df["duration_ms"].mean())

# max_ms = df["duration_ms"].max()
# min_ms = df["duration_ms"].min()
# print(max_ms - min_ms)

# print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"]))

# print(df.groupby('playlist_genre')["duration_ms"].max())

# print(df.query("track_artist=='Ricky Martin'"))

# mean_val = df["duration_ms"].mean()

# print(df.query("duration_ms > @mean_val"))