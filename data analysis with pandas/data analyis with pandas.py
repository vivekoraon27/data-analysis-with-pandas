import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print("DataFrame Head:")
print(df.head())

# Get basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Calculate the average age
average_age = df['Age'].mean()
print(f"\nAverage Age: {average_age}")

# Calculate the average salary
average_salary = df['Salary'].mean()
print(f"Average Salary: {average_salary}")

# Find the maximum salary
max_salary = df['Salary'].max()
print(f"Maximum Salary: {max_salary}")

# Find the minimum age
min_age = df['Age'].min()
print(f"Minimum Age: {min_age}")

# Display basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())