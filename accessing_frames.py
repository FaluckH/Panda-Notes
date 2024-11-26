import pandas as pd

df = pd.read_excel("dev_rankings.xlsx")

print(df)

df = df.set_index("Languages")
print(df)

print(df.loc["Python":"HTML":1:["Ranking 2022","Ranking 2019":2])
      
print(df.iloc[3])

print(df.at["HTML","Ranking 2023"])

print(df.head(2))