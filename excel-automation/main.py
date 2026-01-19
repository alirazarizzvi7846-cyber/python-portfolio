import pandas as pd

df = pd.read_excel("Book.xlsx")

df.columns = df.columns.str.strip().str.lower()
df.dropna(how="all", inplace=True)

# Save cleaned file
df.to_excel("cleaned_output.xlsx", index=False)

print("Excel file cleaned successfully!")