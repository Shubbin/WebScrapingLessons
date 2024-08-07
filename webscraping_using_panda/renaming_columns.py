import pandas as pd

# Read the CSV file from the URL
df_premier21 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E0.csv")


# Print the columns to check the available column names
print(df_premier21.columns)


# Rename the columns correctly
df_premier21.rename(columns={
    "FTHG": "Home_Goals",
    "PCAHA": "mad oh",
    "PCAHH": "unknown",
    "FTAG": "Away_Goals"
}, inplace=True)

# Print the DataFrame
print(df_premier21)
