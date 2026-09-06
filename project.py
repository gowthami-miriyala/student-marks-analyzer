# Student Marks Analyzer

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Number of students
n = int(input("Enter number of students: "))

names = []
marks = []

# Taking student details
for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    names.append(name)
    marks.append(mark)


# Display student report
print("\n========== STUDENT REPORT ==========")

for i in range(n):
    grade = get_grade(marks[i])

    print("Name  :", names[i])
    print("Marks :", marks[i])
    print("Grade :", grade)
    print("------------------------------------")


# Calculate total and average
total = sum(marks)
average = total / n

print("\n========== CLASS DETAILS ==========")
print("Total Marks   :", total)
print("Average Marks :", average)


# Find highest marks
highest = max(marks)
highest_index = marks.index(highest)

print("Highest Marks :", highest)
print("Topper        :", names[highest_index])


# Find lowest marks
lowest = min(marks)
lowest_index = marks.index(lowest)

print("Lowest Marks  :", lowest)
print("Lowest Student:", names[lowest_index])


# Search student
print("\n========== SEARCH STUDENT ==========")

search_name = input("Enter student name to search: ")

if search_name in names:
    index = names.index(search_name)

    print("\nStudent Found!")
    print("Name  :", names[index])
    print("Marks :", marks[index])
    print("Grade :", get_grade(marks[index]))

else:
    print("Student not found!")


# Ranking students
students = []

for i in range(n):
    students.append([names[i], marks[i]])


# Sort according to marks
students.sort(key=lambda x: x[1], reverse=True)


print("\n========== STUDENT RANKING ==========")

rank = 1

for student in students:
    print(
        "Rank", rank,
        ":", student[0],
        "-", student[1],
        "-", get_grade(student[1])
    )

    rank += 1


print("\n========== PROGRAM END ==========")
