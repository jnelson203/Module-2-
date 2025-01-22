#Jayden Nelson
#Module 2 Lab - Case Study: if.. else and while
#My application takes a students name and GPA as input to decide whether they make the Dean's List or Honor Roll.

while True:
    lastName = input("Please state your last name: ")
    if lastName == "ZZZ":
        break
    else:
        print(f"Last Name: {lastName}")

    firstName = input("Please state your first name: ")
    print(f"First Name: {firstName}")

    try:
        studentGpa = float(input("Enter your GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue

    if studentGpa >= 3.5:
        print("You have made the Dean's List!")
    elif studentGpa >= 3.25:
        print("You have made the Honor Roll!")
    else:
        print("Keep working hard!")