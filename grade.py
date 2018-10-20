def Grade(option):
    if option == "GRADE":
        line = "-"
        grade = float(input("Enter the students grade \t"))
        sStudent = str(input("Enter the students name \t"))
        print(line * 45)
        if grade >= 98:
            print("The grade for " + sStudent + " is an A+")
        elif grade >= 93:
            print("The grade for " + sStudent + " is an A")
        elif grade >= 90:
            print("The grade for " + sStudent + " is an A-")
        elif grade >= 88:
            print("The grade for " + sStudent + " is a B+")
        elif grade >= 83:
            print("The grade for " + sStudent + " is a B")
        elif grade >= 80:
            print("The grade for " + sStudent + " is a B-")
        elif grade >= 78:
            print("The grade for " + sStudent + " is a C+")
        elif grade >= 73:
            print("The grade for " + sStudent + " is a C")
        elif grade >= 70:
            print("The grade for " + sStudent + " is a C-")
        elif grade >= 68:
            print("The grade for " + sStudent + " is a D+")
        elif grade >= 63:
            print("The grade for " + sStudent + " is a D")
        elif grade >= 60:
            print("The grade for " + sStudent + " is a D-")
        elif grade >= 0:
            print("The grade for " + sStudent + " is an E")
            print(sStudent + " is failing this course")
            print(line * 45)
