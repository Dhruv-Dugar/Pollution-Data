import pandas as pd
import numpy as np

data = pd.read_csv("city_hour_cleaned.csv")

print(data)

grouped = data.groupby("City")

def split_data(city_name):
    df = grouped.get_group(city_name)
    print(df)
    return df


choosen_cities = ['Delhi']

for city in choosen_cities:
    df = split_data(city)
    df.to_csv(f"{city}_hour_cleaned.csv", index=False)

# get a summar of the data fram df

print(df.describe())
