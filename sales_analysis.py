import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Keyboard"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Accessories"],
    "Price": [50000, 500, 1500, 52000, 600, 1400],
    "Quantity": [5, 50, 30, 3, 40, 25]
}

df = pd.DataFrame(data)

# Revenue
df["Revenue"] = df["Price"] * df["Quantity"]

# Revenue > 100000
print(df[df["Revenue"] > 100000])

# Sort
sorted_df = df.sort_values("Revenue", ascending=False)
print(sorted_df)

# Max & Min
print("Max Revenue:", df["Revenue"].max())
print("Min Revenue:", df["Revenue"].min())

# Accessories
print(df[df["Category"] == "Accessories"])

# Increase Electronics price
df.loc[df["Category"] == "Electronics", "Price"] *= 1.10
print(df)

# Total Laptop Revenue
laptop_total = df[df["Product"] == "Laptop"]["Revenue"].sum()
print("Total Laptop Revenue:", laptop_total)
