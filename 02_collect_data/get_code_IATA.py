import pandas as pd
import json

# data collecting in json file IATA_airports_list
with open("../01_raw_data/IATA_airports_list.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# dataframe transformation
df = pd.json_normalize(data, max_level=2)

# removing unnecessary columns
df.drop(columns=["nameEn", "active" ,"acceptingComplaints", "elevationFeet",
                "website" ,"wikipediaLink" ,"cityId", "city.id", "city.nameEn", 
                "city.countryId", "city.country.id", "city.country.nameEn", "country"], inplace=True)

# renaming columns
change_columns_names = {"nameFr" : "aeroport_name",
                        "city.nameFr" : "city",
                        "city.country.nameFr" : "country"}

df = df.rename(change_columns_names, axis = 1)

# Save IATA data in csv file
df.to_csv("../01_raw_data/IATA_airports_list.csv", index=False)