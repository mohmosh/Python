import pandas as pd

# Create a DataFrame with 3 students
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 19],
    "Grade": [45, 78, 90]
}

df = pd.DataFrame(data)

# Add "Passed" column (True if grade > 50)
df["Passed"] = df["Grade"] > 50

print("Full DataFrame:")
print(df)

# Filter and display only students who passed
passed_students = df[df["Passed"]]
print("\nStudents who passed:")
print(passed_students)
