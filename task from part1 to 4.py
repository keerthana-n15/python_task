# part 1 – List

# Create a list of 10 numbers and print:
# Largest number
# Smallest number
# Sum of all numbers
# Accept 8 student marks in a list and print only the marks greater than 75.
# Remove all duplicate elements from a list without using set().
# Reverse a list without using the reverse() method.
# Find the second largest element in a list.

numbers = [10, 25, 5, 40, 18, 90, 60, 75, 35, 50]

print("Numbers:", numbers)
print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))
print("Sum:", sum(numbers))
print("Second Largest:", sorted(numbers)[-2])
print("Reverse List:", list(reversed(numbers)))
print("Without Duplicates:", list(dict.fromkeys(numbers)))


# Part 2 – Tuple (4 Questions)

# Create a tuple of five cities and print each city using a loop.
cities = ("Chennai", "Madurai", "Coimbatore", "Trichy", "Salem")
print("Cities:")

for city in cities:
    print(city)

    

# Count how many times a given value appears in a tuple.
numbers = (10, 20, 30, 20, 40, 20, 50)
value = int(input("Enter number to count: "))
count = numbers.count(value)
print(value, "appears", count, "times")



# Find the index of an element entered by the user.
city = input("Enter city name: ")
if city in cities:
    print("Index:", cities.index(city))
else:
    print("City not found")



# Convert a tuple into a list, add a new value, and convert it back to a tuple.
city_list = list(cities)
new_city = input("Enter new city: ")
city_list.append(new_city)
cities = tuple(city_list)
print("Updated Tuple:")
print(cities)




# Part 3 – Dictionary 

# Store student details (Name, Age, Department) in a dictionary and print them.
student = {
    "Name": "riya",
    "Age": 20,
    "Department": "CSE"
}
print("Student Details")
for key, value in student.items():
    print(key, ":", value)



# Count the frequency of each character in a string using a dictionary.
text = input("\nEnter a string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)



# Create a dictionary of employee salaries and print the highest-paid employee.
employees = {
    "Rahul": 40000,
    "Anita": 55000,
    "Karthik": 70000,
    "Priya": 60000
}

highest_employee = max(employees, key=employees.get)

print("\nHighest Paid Employee:", highest_employee)
print("Salary:", employees[highest_employee])



# Update the salary of a given employee.
name = input("\nEnter employee name to update: ")
if name in employees:
    salary = int(input("Enter new salary: "))
    employees[name] = salary

print(employees)



# Delete a key from a dictionary entered by the user.
name = input("\nEnter employee name to delete: ")
if name in employees:
    del employees[name]

print(employees)



# Print only the keys and only the values separately.
print("\nKeys")
for key in employees.keys():
    print(key)

print("\nValues")
for value in employees.values():
    print(value)

    students = {
    "S101": {"Name": "Rahul", "Department": "CSE", "Mark": 85},
    "S102": {"Name": "Anita", "Department": "ECE", "Mark": 92},
    "S103": {"Name": "Karthik", "Department": "IT", "Mark": 78}
}

    

# Part 4 – Nested Dictionary (5 Questions)

# Store details of three students in a nested dictionary.
print("Student Details")
for student_id, details in students.items():
    print(student_id, details)



# Find the student with the highest mark.
highest_student = max(students, key=lambda student: students[student]["Mark"])
print("\nHighest Mark Student")
print(students[highest_student])



# Update the department of one student.
student_id = input("\nEnter Student ID to Update Department: ")

if student_id in students:
    department = input("Enter New Department: ")
    students[student_id]["Department"] = department



# Print all students whose marks are above 80.
print("\nStudents Above 80")

for student_id, details in students.items():
    if details["Mark"] > 80:
        print(details["Name"], details["Mark"])


# Add a new student to the nested dictionary.
student_id = input("\nEnter New Student ID: ")
name = input("Enter Name: ")
department = input("Enter Department: ")
mark = int(input("Enter Mark: "))
students[student_id] = {
    "Name": name,
    "Department": department,
    "Mark": mark
}

print("\nUpdated Student List")

for student_id, details in students.items():
    print(student_id, details)