# B8_Mini_Assignment_1---Student Score Analyzer


# SCHOOL MANAGEMENT BACKEND SYSTEM
# This is a backend program that stores student data,
# calculates performance, and generates reports.

# Create an empty list to store all student records
students = []


#================================
#TASK 1: INPUT COLLECTION & VALIDATION
#================================

#Start an infinite loop to keep collecting students
while True:

    # Ask user to enter student name or "done" to stop
    name = input("Enter student name (or 'done'): ").strip()

    # If user types "done", exit the loop
    if name.lower() == "done":
        break

    # If user enters empty name, show error and restart loop
    if name == "":
        print("Name cannot be empty.")
        continue

    # Create an empty list to store 3 scores for each student
    scores = []

    # Loop 3 times to collect 3 scores
    for i in range(1, 4):

        # Keep asking until valid score is entered
        while True:
            try:
                # Ask user for score and convert to integer
                score = int(input(f"Enter score {i}: "))

                # Check if score is outside valid range
                if score < 0 or score > 100:
                    print("Invalid score. Enter 0–100.")
                else:
                    # Add valid score to list
                    scores.append(score)

                    # Exit score validation loop
                    break

            # Handle non-numeric input
            except ValueError:
                print("Please enter a valid integer.")

    # Create a dictionary to store student data
    student = {
        "name": name,        # student name
        "scores": scores,    # list of 3 scores
        "average": 0,        # placeholder for average
        "grade": "",         # placeholder for grade
        "status": ""         # placeholder for PASS/FAIL
    }

    # Add student dictionary to main students list
    students.append(student)

    # Confirm student was added
    print("Student added.\n")


# ================================
# TASK 2: AVERAGE & GRADE CALCULATION
# ================================

# Loop through each student in the list
for student in students:

    # Calculate average score
    avg = sum(student["scores"]) / 3

    # Round average to 1 decimal place
    avg = round(avg, 1)

    # Store average inside student dictionary
    student["average"] = avg

    # Assign grade based on average
    if avg >= 80:
        student["grade"] = "A"
    elif avg >= 65:
        student["grade"] = "B"
    elif avg >= 50:
        student["grade"] = "C"
    elif avg >= 40:
        student["grade"] = "D"
    else:
        student["grade"] = "F"

    # Assign PASS or FAIL based on average
    if avg >= 50:
        student["status"] = "PASS"
    else:
        student["status"] = "FAIL"


# ================================
# TASK 3: TOP PERFORMER (NO max())
# ================================

# Initialize variables for top student tracking
top_student = None      # stores student with highest average
top_average = 0         # stores highest average value

# Loop through all students
for student in students:

    # If current student's average is higher than stored highest
    if student["average"] > top_average:

        # Update highest average
        top_average = student["average"]

        # Store student as top performer
        top_student = student


# ================================
# TASK 4: SPECIAL SCORE CONDITIONS
# ================================

# List to store students with any failing score (<40)
failing_score_students = []

# List to store students with perfect score (100)
perfect_score_students = []

# Loop through all students
for student in students:

    # Check each score for failing condition
    for score in student["scores"]:

        # If any score is below 40
        if score < 40:

            # Add student name to failing list
            failing_score_students.append(student["name"])

            # Stop checking further scores for this student
            break

    # Check each score for perfect score condition
    for score in student["scores"]:

        # If any score is exactly 100
        if score == 100:

            # Add student name to perfect score list
            perfect_score_students.append(student["name"])

            # Stop checking further scores for this student
            break


# Remove duplicate names using set (sets cannot have duplicates)
failing_score_students = list(set(failing_score_students))
perfect_score_students = list(set(perfect_score_students))


# ================================
# TASK 5: CLASS AVERAGE
# ================================

# Initialize total sum of averages
total = 0

# Loop through each student
for student in students:

    # Add each student's average to total
    total += student["average"]

# Calculate class average
# If students exist → divide total by number of students
# If no students → set class average to 0
class_average = round(total / len(students), 1) if students else 0


# ================================
# TASK 6: BACKEND REPORT
# ================================

# Print report header
print("\n========================================")
print("STUDENT PERFORMANCE REPORT")
print("========================================\n")

# Loop through students with numbering starting from 1
for i, student in enumerate(students, start=1):

    # Print student number and name
    print(f"{i}. {student['name']}")

    # Print list of scores
    print(f"   Scores: {student['scores']}")

    # Print average score
    print(f"   Average: {student['average']}")

    # Print grade
    print(f"   Grade: {student['grade']}")

    # Print PASS/FAIL status
    print(f"   Status: {student['status']}\n")

# Print separator line
print("========================================")

# Get top student name safely
top_name = top_student["name"] if top_student else "None"

# Get top average safely
top_avg = top_average if top_student else 0

# Print class average
print(f"Class Average:{class_average}")

# Print top performer if exists
if top_student:
    print(f"Top Performer:{top_name} ({top_avg})")
else:
    print("Top Performer:None")

# Print students with failing scores
if failing_score_students:
    print(f"Students with failing scores: {', '.join(failing_score_students)}")
else:
    print("Students with failing scores: None")

# Print students with perfect scores
if perfect_score_students:
    print(f"Students with perfect scores: {', '.join(perfect_score_students)}")
else:
    print("Students with perfect scores: None")

# Print final separator
print("========================================")


# ================================
# TASK 7: SEARCH FEATURE
# ================================

# Start infinite loop for searching students
while True:

    # Ask user to enter student name or exit
    search = input("\nEnter a student name to view details (or 'exit' to quit): ").strip()

    # Exit search loop if user types exit
    if search.lower() == "exit":
        print("Goodbye!")
        break

    # Flag to track if student is found
    found = False

    # Loop through all students
    for student in students:

        # Compare names ignoring case
        if student["name"].lower() == search.lower():

            # Print student details
            print(f"\nName:    {student['name']}")
            print(f"Scores:  {student['scores']}")
            print(f"Average: {student['average']}")
            print(f"Grade:   {student['grade']}")
            print(f"Status:  {student['status']}\n")

            # Mark as found
            found = True

            # Stop searching further
            break

    # If no student matched the search
    if not found:
        print("Student not found")
        
  
  
  
  
  # ------------------------------FLOW OF THE PROGRAM-----------------------------      
# Start
#  ↓
# Collect student names
#  ↓
# Validate scores
#  ↓
# Store student records
#  ↓
# Calculate averages
#  ↓
# Assign grades
#  ↓
# Determine PASS/FAIL
#  ↓
# Find top performer
#  ↓
# Find failing/perfect scores
#  ↓
# Calculate class average
#  ↓
# Generate report
#  ↓
# Search for students
#  ↓
# Exit



#---------------------------ASSIGNMENT 2a------------------------------------------
# Grade Summary

# def grade_summary(*args, subject="General"):
#     """
#     Accepts any number of scores and returns a summary
#     showing the subject, number of scores, highest score,
#     lowest score, and average score.
#     """

#     # Check if no scores were provided
#     if len(args) == 0:
#         return "No scores provided."

#     # Initialize highest and lowest using first score
#     highest = args[0]
#     lowest = args[0]

#     # Variable to keep track of total
#     total = 0

#     # Loop through each score
#     for score in args:

#         # Add to total
#         total += score

#         # Check highest
#         if score > highest:
#             highest = score

#         # Check lowest
#         if score < lowest:
#             lowest = score

#     # Calculate average
#     average = total / len(args)

#     # Return formatted result
#     return (
#         f"Subject: {subject} | "
#         f"Scores: {len(args)} | "
#         f"Highest: {highest} | "
#         f"Lowest: {lowest} | "
#         f"Average: {average:.1f}"
#     )


# print(f"==================================================================================")
# print(grade_summary(80, 90, 70, 60, 92, subject="Mathematics"))
# print(grade_summary(90, 76, 88))
# print(grade_summary())
# print(f"==================================================================================")






# # --------------------------ASSIGNMENT 2b--------------------------------------

# Define a function called student_card
# It accepts:
# - name: the student's name
# - cohort: the student's cohort number
# - **kwargs: any extra named information (track, level, email, etc.)
# def student_card(name, cohort, **kwargs):

#     """
#     Prints a formatted student card containing
#     the student's name, cohort, and any additional fields.
#     """

#     # Print the student's name
#     # 'Name'.ljust(12) makes the word "Name" occupy exactly 12 spaces
#     print(f"{'Name'.ljust(12)}: {name}")

#     # Print the student's cohort
#     # 'Cohort'.ljust(12) makes the word "Cohort" occupy exactly 12 spaces
#     print(f"{'Cohort'.ljust(12)}: {cohort}")

#     # Loop through all the extra named arguments
#     # kwargs.items() returns key-value pairs
#     for key, value in kwargs.items():

#         # Capitalize the first letter of the key
#         # ljust(12) ensures the label is exactly 12 characters wide
#         print(f"{key.capitalize().ljust(12)}: {value}")

# # Call the function for the first student
# student_card(
#     "Ada Okafor",                  # name
#     3,                             # cohort
#     track="Data Engineering",      # extra field
#     level="Intermediate",          # extra field
#     email="ada@gmail.com"          # extra field
# )

# # Print an empty line to separate outputs
# print("===============================================")

# # Call the function for the second student
# student_card(
#     "John Bello",                  # name
#     2,                             # cohort
#     track="Cyber Security",        # extra field
#     level="Beginner"               # extra field
# )


# # Print another empty line
# print("===============================================")

# # Call the function for the third student
# student_card(
#     "Fatima Musa",                 # name
#     1,                             # cohort
#     email="fatima@gmail.com",      # extra field
#     track="Python Programming",    # extra field
#     level="Intermediate",          # extra field
#     country="Nigeria"              # extra field
# )    
        