import pandas as pd

df = pd.read_csv("spotify_songs.csv")

print(df)

# print(df.shape)

# print(df.columns)

# print(df.info)

# print(df["playlist_genre"].value_counts())

# print(df["playlist_genre"].mode())

# print(df["playlist_genre"].mode()[0])

# print(df[duration_ms].mean())

print(df.sort_values(by=["duration_ms"], ascending=False))

print(df.query("track_artist=='Ricky Martin'"))

mean_val = df["duration_ms"].mean()