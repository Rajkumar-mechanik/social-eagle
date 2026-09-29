def student_grade():
    try:
        mark = float(input("Enter the student's mark (0-100): "))

        # Check whether the mark is within the valid range
        if mark < 0:
            print(f"Invalid mark: {mark}. Mark cannot be below 0.")
        elif mark > 100:
            print(f"Invalid mark: {mark}. Mark cannot be above 100.")
        else:
            # Determine the grade
            if mark >= 90:
                grade = "A"
            elif mark >= 80:
                grade = "B"
            elif mark >= 70:
                grade = "C"
            elif mark >= 60:
                grade = "D"
            else:
                grade = "E"

            print(f"Entered mark: {mark}")
            print(f"Resulting grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")


# Run the program
student_grade()