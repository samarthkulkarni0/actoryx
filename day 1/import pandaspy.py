import pandas as pd

file_path = input("Enter CSV file path: ")

df = pd.read_csv(file_path)

print(df.head(10))