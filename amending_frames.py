import pandas as pd 

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
# rankings = pd.Series([3,1,2,4])

# df = pd.DataFrame({
#     "Languages": languages,
#     "Ranking": rankings
# })

# # df.loc[4] = ["PHP", 11]
# # df.loc[3.5] = ["KESL", 20]

# # df = df.sort_index()
# # df = df.reset_index(drop=True)
# print(df)

# new_data = pd.DataFrame({
#     "Languages" : ["PHP"],
#     "Ranking" : [11]
# })

# df.loc[5] = ["Java", 7]
# df.loc[6] = ["TypeScript", 5]

# df = pd.concat([df,new_data], ignore_index=True)

# df["Ranking 2022"] = [4,1,2,3,10,6,5]
# print(df)

# new_data = pd.DataFrame({"Ranking 2020":[4,1,2,3,10,6,5],"Ranking 2019":[4,1,2,3,10,6,5] })
# df = pd.concat([df,new_data], axis=1)

# df.insert(3,"Ranking 2021", [4,1,2,3,10,6,5 ])
# df.rename(columns={"Ranking": "Ranking 2023"}, inplace=True)

# print(df)

# df = df.set_index("Languages")

# print(df)
-------------- activity 2 ------------------------------

planets = pd.Series(["Saturn", "Mars", "Mercury",])
Average Temperature = pd.Series([-178,-65,167])

df = pd.DataFrame({
    "Planets": planets,
    "Average Temperature": average_temperature
})

print(df)

new_data = pd.DataFrame({
    "Languages" : ["PHP"],
    "Ranking" : [11]
})

df.loc[5] = ["Java", 7]
df.loc[6] = ["TypeScript", 5]

df = pd.concat([df,new_data], ignore_index=True)

df["Ranking 2022"] = [4,1,2,3,10,6,5]
print(df)

new_data = pd.DataFrame({"Ranking 2020":[4,1,2,3,10,6,5],"Ranking 2019":[4,1,2,3,10,6,5] })