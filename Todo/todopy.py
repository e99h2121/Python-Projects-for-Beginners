# using idea from:
# https://github.com/ayrahisham/students-record-management-system/blob/master/A4.py

# Write a python program to
# 1. Load a student csv data file into the program memory.
# 2. Allow the user to perform the following with menu selection.
# a. Insert a new student
# b. Delete a student
# c. Save the updated student information back to the data csv file.

def menu () :
    print ("TODO管理")
    print ("1. TODOを登録する")
    print ("2. TODOを削除する")
    print ("3. ファイルに保存して終了する")
    choice = input ("番号を選択: ")
    
    return choice

partition = "\n--------------------------------------------------------\n"

# Error checking 2
# Check that file exists
# The program will check if the file exists
# Will create file if file does not exist 
def createFile (filePath) :
    import csv     
    try:
        file = open (filePath, 'r')
    except FileNotFoundError:
        file = open (filePath, 'w') 

# Extracting current data in file into dictionary for temp storage
def copyContentsFromFile (filePath) :
    import csv

    todoFile = {}
    todoID = []
    todo = []
    
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        size = noOfRecords (filePath)
        for i in range (0, size) :
            for row in reader :
                todoID.append (row ['todo_id'])
                todo.append (row ['todo'])
        # Append list data to dictionary
        for i in range (0, len (todoID)) :
            todoFile [todoID [i]] = {}
            todoFile [todoID [i]].update ({"todo" : todo [i]})

    return todoFile

# Display dictionary data after manupulation
def displayDictData (sdict) :
    print ("{0:<20} | {1:<20}".format ("todo", "todo ID"))

    for elements in sdict.keys () :
        info = sdict.get (elements)
        fname = info["todo"]
        print ("{0:<20} | {1:<20}".format (fname, elements))
    print ()
    

# Matching the valid letter for every student id
def matchletter (rnum) :
    if (rnum == 0) :
        letter = 'B'
    elif (rnum == 1) :
        letter = 'C'
    elif (rnum == 2) :
        letter = 'D'
    elif (rnum == 3) :
        letter = 'E'
    elif (rnum == 4) :
        letter = 'F'
    elif (rnum == 5) :
        letter ='G'
    elif (rnum == 6) :
        letter = 'H'
    elif (rnum == 7) :
        letter = 'I'
    elif (rnum == 20) :
        letter = 'J'
    elif (rnum == 9) :
        letter = 'K'
    elif (rnum == 10) :
        letter = 'L'
    else :
        letter = "NULL"
    return letter

# Error checking 5
# Check for invalid student id letter
# The program will check if the user had entered valid student id before writing to file.
# Will prompt user to enter correct student id with the correct letter
def isValidStudentIDLetter (sid) :
    letterok = False
    # Multiply each of the numbers with 2, 7, 6, 5, 4, 3, 2
    # in sequence.
    total = 0
    one = int (sid [1]) * 2
    two = int (sid [2]) * 7
    three = int (sid [3]) * 6
    four = (int (sid [4])) * 5
    five = int (sid [5]) * 4
    six = int (sid [6]) * 3
    seven = int (sid [7]) * 2
    
    # Sum up the multiplication results
    total =  one + two + three + four + five + six + seven 
    # Divide the sum by 11 and get the remainder
    remainder = total % 11

    alpha = matchletter (remainder)
    if (not alpha == "NULL") :
        if (sid [len (sid) - 1] == alpha) :
            letterok = True
            
    return letterok, alpha

# Error checking 6
# Check for student id is in dictionary for deletion
# The program will check if the user had entered non-existing student id before writing to file.
# Will prompt user to enter another student id
def checkStudentID (sid, sdict) :
    for elements in sdict.keys () :
        if (elements == sid) :
            return True
    return False

# Error checking 7
# Check for student id is in dictionary for insertion
# The program will check if the user had entered duplicated student id before writing to file.
# Will prompt user to enter another student id
def checkSameStudentID (sid, sdict) :
    for elements in sdict.keys () :
        if (elements == sid) :
            return False
    return True

def insertTodo (sdict) :
    print ("Insert a new TODO")    
    fname = input ("Enter todo: ")
    sid = input ("Enter todo ID: ")
    return fname, sid

def deleteTodo (sdict) :
    idok = False
    foundok = False
    
    while (idok == False) :
        sid = input ("Enter todo ID: ")
        idok, reason = isValidStudentIDFormat (sid)
        if (idok == False) :
            print (reason)
        else :
            idok, letter = isValidStudentIDLetter (sid)
            if (idok == False) :
                print ("Invalid last letter, student ID should be " + sid [: len(sid)-1] + letter)    
            else :
                idok = checkStudentID (sid, sdict)
                if (idok == False) :
                    print ("Student ID not found")
    
    del sdict [sid]
    return sdict

# No of records in file
def noOfRecords (filePath) :
    import csv
    
    with open(filePath, 'r') as csvfile:
        csv_dict = [row for row in csv.DictReader(csvfile)]
        size = len (csv_dict)
    
    return size        

def writeToFile (filePath, sdict) :
    import csv
    # Empty contents of file for writing of dictionary data to file
    open(filePath, 'w').close()
    with open(filePath, 'a', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'student_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Error checking 8
        # Check for no of records in file
        # The program will check no of records to write headers for file
        # Will print file headers
        # Else will copy from dictionary to file
        if (noOfRecords(filePath) == 0) :
            # If file is empty, write headers to file
            writer.writeheader ()
            for sid in sdict.keys () :
                todoid = sdict.get (sid)
                todo = todoid.get ("todo")
                writer.writerow ({'todo': todo, 
                                  'todo_id': sid})
        else :
            for sid in sdict.keys () :
                todoid = sdict.get (sid)
                todo = todoid.get ("todo")
                writer.writerow ({'todo': todo, 
                                  'todo_id': sid})
                
# Error checking 9
# Check for correct filename
# The program will check filename exists in current folder
# Will error message and prompt user to input again
# Else will copy to dictionary from file
def fileExists (filePath) :
    import os.path
    return os.path.exists(filePath)  

def main () :
    file = "data.csv"      
    proceed = True
    sfile = {}
    tymsg = "ファイルを保存しました。\nThank you for using Student Records Management System"
    
    filePath = input ("ファイル名を入れてください: ")
    ok = fileExists (filePath)
    print ()
    if (ok == False) :
        print ("ファイルが存在しません。既定値でファイルを作成しました。(data.csv)\n")
        filePath = file
        createFile (filePath)
    else :
        print ("File is copied into dictionary for manupulation.\n")
   
    sfile = copyContentsFromFile (filePath) 
    
    while (proceed == True) :
        choice = menu ()
        
        #Error checking 3
        #Check for invalid menu choice selection.
        #The program will check if the user had entered 1 2 or 3 in the main menu selection.
        if (choice.isdigit () == True) :
            if (int (choice) == 1) :
                print (partition)
                print ("List of Todos")
                displayDictData (sfile)                
                fname, sid = insertTodo (sfile)
                # To update valid inserted values in dictionary after valid checking
                sfile [sid] = {}
                sfile [sid].update ({"todo" : fname})
                print ("\nNew todo Record Inserted")
                print ()
                print ("List of Todos")
                displayDictData (sfile)
                
            elif (int (choice) == 2) :
                print (partition)
                print ("List of todos")
                displayDictData (sfile) 
                # To return dictionary after deletion
                sfile = deleteStudent (sfile)
                print ("\nTodo Record Deleted")
                print ()
                print ("List of Todos")
                displayDictData (sfile)                 
                    
            elif (int (choice) == 3) :
                print (partition)
                proceed = False
                # To copy finalized dictionary data to file
                writeToFile (filePath, sfile)
                print (tymsg)
            
            #If an invalid choice (not 1, 2 or 3) is enter, the user is asked to re-enter the choice again
            else :
                print ("Invalid choice, please re-enter again")
                print (partition)
        #If an invalid choice (alpha) is enter, the user is asked to re-enter the choice again
        else :
            print ("Invalid choice format, please re-enter again")
            print (partition)
            
        if (proceed == True) :
            continueok = input ("\nContinue: (Y/N): ")
            print (partition)
                
            if (continueok == 'N' or continueok == 'n') :     
                proceed = False
                # To copy finalized dictionary data to file
                writeToFile (filePath, sfile)               
                print (tymsg)

main()
