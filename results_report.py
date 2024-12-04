# import pandas as pd
# from ydata_profiling import ProfileReport

# df = pd.read_csv("results.csv")

# # profile = ProfileReport(df, title = "International Results")

# # profile.to_file('results_report.html')

# import pandas as pd

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

import pandas as pd
import matplotlib.pyplot as plt 

download_speed=[
        33.40, 32.16, 32.38, 40.06, 38.68, 39.74, 38, 39.39, 43.71, 41.89,
        40.64, 44.20, 45.29, 43.11, 42.82, 43.02, 41.66, 44.17, 46.67, 
        42.58, 41.58, 44.53, 43.63, 42.98, 40.55, 45.07, 33.90, 41.70, 42.48, 
        45.96, 37.44, 42.09, 43.63, 42.58, 46.07, 46.36, 41.68, 39.20, 43.13, 43.41, 
        40.35, 44.29, 45.83, 44.48, 44.90, 40.45, 44.59, 44.95, 45.11, 42.60, 39.38, 43.82, 
        44.04]

df = pd.DataFrame({"Download Speed" : download_speed})
print(df.describe())
plt.boxplot(download_speed, vert=0)
plt.show()