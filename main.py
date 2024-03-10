def listAllCourses(courses):  #Done 1 ,list all the courses!
    for c in courses: #for every item in the text file.
        print(c)  #then when we will call the function we call it with a list we did strip and split

#_____________________________________________________________________________________________

def listNonEmptyCourses(courses):  # Done 2 -List all the course that have at least one student registered.
    for c in courses: #for loop goes into the file
        num_of_students = int(c[3]) #indexing and converting a string to a integer
        if num_of_students != 0: #if the input is not equal
            print(c)  #print all the course that have at least one student registered

#_____________________________________________________________________________________________

def addCourse(courses):  # 3_Done! : Add a new course to course.txt
    f = open("course.txt", 'a')  #open the file in append mood
    for line in courses:
        cols = line.strip('\n').split(";") #strip lines to get rid of unseen characherts or \n , and split them to seperate them
        courseCode = cols[0]  #indexing
        courseName = cols[1]
        courseInstc = cols[2]
        numOfStudents = int(cols[3]) #convert a string to integer
        courseDict[courseCode] = [courseName, courseInstc, numOfStudents] #courseDict is a dictionary in global
    course_code = str(input("\nEntre the course code please: ")).upper()

    if course_code not in courseDict.keys():
        course_name = str(input("\nEntre the course name please:"))
        instructor_name = str(input("\nEntre the doctor name please:"))
        numOfStudents = str(0)  # because it's a new course , so it will start with 0
        addACourse = ("\n", course_code, ";", course_name, ";", instructor_name, ";", numOfStudents)  # indexing
        b = ''.join(addACourse)  # using join string method.
        f.write(b)

    f.close()

#_____________________________________________________________________________________________

def searchCourseCode(courses): #4_Done!  search a course by a course code
    courses = open("course.txt","r")
    courseDict = {} #an empty dic

    for line in courses:
        cols = line.strip('\n').split(";")
        courseCode = cols[0]
        courseName = cols[1]
        courseInstc = cols[2]
        numOfStudents = int(cols[3])
        courseDict[courseCode] = [[courseName],[courseInstc],[numOfStudents]]

    course_code = input("\nPlease Entre the Course Code:").upper()
    key = course_code #assigning course_code to a variable called key
    if key in courseDict.keys(): #if the key which isthe input is in course dictionary in keys print the following
        print("the course is there!")
        print(courseDict[key])
    else:
        print("Sorry, the course code you enrolled does not exist!")
    courses.close()

#_____________________________________________________________________________________________

def searchCourseName(courses): #5_ Done search a course by course name!
    course_name = input("Please Entre the name of the course: ")
    for i in courses:
        if course_name == i[1]: #if the input is equal to index no 1 which is course name print the item
            return (i)
    return("The course you chose does not exist! ") #if we look for the item in all file and we couldn't see it we go out of the loop and print doesnt exist

#_____________________________________________________________________________________________

def register_student_to_course(courses, students):  #6_Done register a student in course
    coursesFile = open("course.txt","w")
    studentsFile = open("student.txt","w")
    course_code = input("Please Enter The Course Code:   ")
    student_id = input("Please Enter The Student id:   ")

    for s in students:
        if student_id == s[0]: #if the input is equal to the index 0 which is student id
            s[2] += "," + course_code #go to index 2 which is course code and add the input(course code in the file)
            break
    for c in courses:
        if course_code == c[0]: #if course code is equall to index 0 (which is course code in the file)
            num_student = int(c[3]) + 1 #add one to the index 3 which is the num of students!
            c[3] = str(num_student) #convert it agian to string because everything in text file is string

    for course in courses:
        courseDetailes = ";".join(course) + "\n" #join every item in text file with ;
        coursesFile.write(courseDetailes) #we will write the info in the file after seperating them with ;
    for student in students:
        studentDetailes = ";".join(student) + "\n" #join every item in text file with ;
        studentsFile.write(studentDetailes)
    studentsFile.close()
    coursesFile.close()

#_____________________________________________________________________________________________

def listAllStudentsWithCourses(students): #7 - Done prints students name then the courses he has
    students = open("student.txt", "r")
    for i in students.readlines(): #use readlines to read the file and put it in a list
        b = i.strip().split(";")
        stuName = b[1] #indexing the student name to index no 1
        stuCourse = b[2] #indexing the student course to index no 2
        print(stuName,":","\n", stuCourse) #to print student name and under her or his name the courses that he\she registered in
    students.close()

#_____________________________________________________________________________________________

def most_crowded_courses(): #8_ List top 3 most crowded courses
    courses = open("course.txt", "r")
    myCourses = courses.readlines()
    myList = []
    for i in range(len(myCourses)):
        values = myCourses[i].strip().split(";")
        a = values[0], values[1], int(values[3])
        myList.append(a)
    myStortedList = []
    while len(myStortedList) != 3:
        theCourse = myList[0]
        max = 0
        for i in myList:
            if i[2] > max:
                max = i[2]
                theCourse = i
        myStortedList.append(theCourse)
        myList.remove(theCourse)

    return myStortedList
#________________________________________________________________________

def most_student_have_course_registirations(): #9_List top 3 students with the most course registrations
    students = open("student.txt", "r")
    myStudents = students.readlines()
    myList = []
    for i in range(len(myStudents)):
        values = myStudents[i].strip("\n").split(';') #seperate the items in each line
        coursesnumber = len(values[2].split(",")) #to reach course codes that each student register in and use split to seperate them with (,)
        a = values[0], values[1], int(coursesnumber)
        myList.append(a)
    myStortedList = []
    while len(myStortedList) != 3:  # to give just top 3 values
        theStudent = myList
        max = 0
        for i in myList:
            if i[2] > max:
                max = i[2]
                theStudent = i
        myStortedList.append(theStudent)
        myList.remove(theStudent)

    return myStortedList
#_____________________________________________________________________________________________

courses = open("course.txt" ,"r")
students = open("student.txt", "r")
courseDict = {}
studentsDict = {}

def main():
    global  courses
    global students

    coursesList = [] #an empty list
    for i in courses: #for every elemnt in the file
        l = i.strip("\n").split(";")
        coursesList.append(l) #we will make a list for each line! because it is inside the foor loop

    studentsList = [] #creating an empty list
    for i in students:
        b = i.strip("\n").split(";")
        studentsList.append(b)

    while_value= True
    while while_value: #making the menu that the user will choose from
        print("1.List all the courses") #list all courses from course.txt
        print("2.List all the course that have at least one student registered")
        print("3.Add a new course")
        print("4.Search a course by course code")
        print("5.Search a course by name")
        print("6.Register a student to a course")
        print("7.List all the students their registered courses")
        print("8.List top 3 most crowded courses")
        print("9.List top 3 students with the most course registrations")
        print("10.For Exit option Enter 0")
        option = int(input("\nPlease choose a number from the menu shown: "))
        if option ==0:
            print("the program is ended")
            break
        elif option ==1:
            listAllCourses(coursesList)
        elif option ==2:
            listNonEmptyCourses(coursesList)
        elif option ==3:
            addCourse(courses)
        elif option ==4:
            searchCourseCode(courses)
        elif option ==5:
            print(searchCourseName(coursesList))
        elif option ==6:
            register_student_to_course(coursesList,studentsList)
        elif option ==7:
            listAllStudentsWithCourses(students)
        elif option ==8:
            my_courses = most_crowded_courses()
            for i in my_courses:
                print(i[1] + ":" + str(i[2]))  #to make it look better
        elif option ==9:
            my_student = most_student_have_course_registirations()
            for i in my_student:
                print(i[1] + ":" + str(i[2])) #to make it look better
    print("")






main()

courses.close()
students.close()

