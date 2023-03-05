import pandas as pd

data = pd.read_csv("city_hour.csv")
print(data)

print(data.dropna())

print("=====================================")

new_data = data.dropna()


new_data.to_csv("city_hour_cleaned.csv", index=False)