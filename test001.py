import pandas as pd

print("Running in container...")

# Create a simple DataFrame with a dictionary
# The keys are the column names and the values are the data

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [24, 27, 22],
    'City' : ['New York', 'Los Angeles', 'Chicago']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Access a column
print("\nNames column:")
print(df['Name'])

# Access a row by index
print("\nFirst row")
print(df.iloc[0])

# Add a new column
df['Salary'] = [70000, 80000, 65000]

# Display the update DataFrame
print("\n DataFrame with Salary column:")
print(df)

# Calculate the mean age
mean_age = df['Age'].mean()
print("\nMean age:", mean_age)

# Save the DataFrame to a CSV file
df.to_csv('people.csv', index=False)
