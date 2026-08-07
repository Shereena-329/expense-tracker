import csv
import csv

students = [
    ["Name", "Mark"],
    ["Anu", 85],
    ["Rahul", 90],
    ["Sneha", 78],
    ["Akhil", 88],
    ["Meera", 92]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Data written successfully.")