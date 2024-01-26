student_list = [{"Name": "Jeffery", "Hometown": "California", "Favorite_food": "Cheesecake"},
                {"Name": "Paul", "Hometown": "Orlando" , "Favorite_food": "Marzipan"},
                {"Name": "Tom", "Hometown": "Ann Arbor", "Favorite_Food": "Lamb Curry"}]

contInput="y"
secondChoice="potato"
def list_names(students):
    for student in students:
        if "Name" in student:
            print(f'{students.index(student) + 1}. {student["Name"]}')
def get_new_student():
    name=input("What is the students name? ")
    newHometown=input("What is the students hometown? ")
    newFavoriteFood=input("What is the students favorite food? ")

    addStudent= {"Name": name,"Hometown": newHometown," Favorite_Food": newFavoriteFood}
    return addStudent
while contInput=="y":
    userInput = input("Which option do you want to do today? (add/view/quit) ")
    userInput = userInput.lower()
    if userInput == "add":
        student_list.append(get_new_student())
        print(student_list[len(student_list)-1])
    elif userInput == "view":
        list_names(student_list)
        secondChoice=int(input("Which student would you like to view?(0-3)"))
        print(student_list[secondChoice]["Name"])
        validInput=False
        while validInput==False:
            thirdChoice=input("Would you like to see the student's favorite food or hometown?")
            thirdChoice=thirdChoice.lower()
            if thirdChoice=="favorite_food":
                print(student_list[secondChoice]["Favorite_food"])
                validInput=True
            elif thirdChoice=="hometown":
                print(student_list[secondChoice]["Hometown"])
                validInput=True
            else:
                print("Invalid input please try again")

        contInput=input("Would you like to continue?(y/n")

    elif userInput == "quit":
        contInput="n"
    else:
        print("Invalid input")
