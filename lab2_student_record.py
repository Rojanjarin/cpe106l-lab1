# Initial Data
student = {
    "id": "2025-001",
    "name": "Juan Dela Cruz",
    "grades": [88, 90, 85]
}

# Calculate Average
average = sum(student["grades"]) / len(student["grades"])
print(f"Average: {average:.2f}")
# 1. Add grades
# Let's add a new grade to the list
student["grades"].append(92)

# 2. Update student info
# Updating the name or ID
student["name"] = "Juan Dela Cruz Jr."

# 3. Display formatted output
# Recalculating average after adding the new grade
new_average = sum(student["grades"]) / len(student["grades"])

print("\n--- Updated Student Record ---")
print(f"ID:      {student['id']}")
print(f"Name:    {student['name']}")
print(f"Grades:  {student['grades']}")
print(f"Average: {new_average:.2f}")