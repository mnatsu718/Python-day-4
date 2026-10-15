grade = {
    "Mizuki" : "A+",
    "Ibuki" : "B",
    "Kai" : "C+"
    "user not found"
}

student = input("Student name?")

if grade.get(student) != None:
    print(student, "got a", grade.get(student))

else:
    print("Student not found.")


def main()
    grade = int(input("What grade did you get?"))

    if grade >= 90:
        print("You got an A!")

    elif grade >= 70:
        print ("You got a B")

    else: print ("You got a C")


#if grades.get(student):