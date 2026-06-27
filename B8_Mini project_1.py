# B8_Mini_Project_1---Student Score Analyzer

# Define a function called get_score that accepts a prompt message
def get_score(prompt):

    # Docstring explains what the function does
    # It is ignored by Python when running the code but useful for documentation
    """
    Ask the user for a valid score between 0 and 100.
    Keeps asking until a valid number is entered.
    """

    # Start an infinite loop to keep asking until valid input is given
    while True:

        # Try block to catch errors like invalid input (e.g. letters instead of numbers)
        try:

            # Ask user for input and convert it into a float
            score = float(input(prompt))

            # Check if score is within valid range (0 to 100)
            if 0 <= score <= 100:

                # If valid, return the score and exit the function immediately
                return score

            else:
                # If score is outside range, show error message
                print("Score must be between 0 and 100. Try again.")

        # If user enters something that cannot be converted to float
        except ValueError:

            # Show error message for invalid input type
            print("Please enter a valid number.")


# Define the main function (this controls the program flow)
def main():

    # Print header message for the program
    print("===== Student Score Analyzer =====")

    # Start a loop to allow multiple students to be processed
    while True:
        
         # Ask for student name
        name = input("Enter student name: ")

        # Collect scores using get_score function
        score1 = get_score("Enter score 1 (0-100): ")

        score2 = get_score("Enter score 2 (0-100): ")

        score3 = get_score("Enter score 3 (0-100): ")

        # Calculate average of the three scores
        average = (score1 + score2 + score3) / 3

        # Check if student passed or failed
        if average >= 50:

            # If average is 50 or more, student passes
            result = "PASS"

        else:
            # If average is below 50, student fails
            result = "FAIL"

        # Print summary header
        print("\n===== STUDENT SUMMARY =====")
        print(f"Student Name: {name}")

        # Print first score
        print(f"Score 1: {score1:.1f}")

        # Print second score
        print(f"Score 2: {score2:.1f}")

        # Print third score
        print(f"Score 3: {score3:.1f}")

        # Print average rounded to 2 decimal places
        print(f"Average: {average:.2f}")

        # Print pass/fail result
        print(f"Result: {result}")

        # Print footer line for clarity
        print("===========================\n")

        # Ask user if they want to process another student (validated input)
        while True:
            another = input("Another student? (y/n): ").lower()

            # Validate input so user cannot accidentally exit with wrong input
            if another in ("y", "n"):
                break
            print("Please enter 'y' or 'n' only.")

        # If user does NOT type "y", stop the loop
        if another != "y":
            break

    # This line runs ONLY after the loop ends
    print("Thank you for using Student Score Analyzer")


# This is the entry point of the program
# It checks whether this file is being run directly or imported

if __name__ == "__main__":

    # If running directly, start the program by calling main()
    main()

    # If this file is imported into another file,
    # main() will NOT run automatically


#------------------- PROGRAM FLOW DIAGRAM-----------------------------

# Start
#  ↓
# Print welcome message
#  ↓
# Get Score 1 (validate)
#  ↓
# Get Score 2 (validate)
#  ↓
# Get Score 3 (validate)
#  ↓
# Calculate average
#  ↓
# Average ≥ 50?
#  ├─ Yes → PASS
#  └─ No  → FAIL
#  ↓
# Print summary
#  ↓
# Another student? (validated y/n input)
#  ↓
#  ├─ y → Repeat
#  └─ n → Exit loop
#  ↓
# Print thank you message
#  ↓
# End

