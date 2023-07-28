#set database
import database

#input if he want to preview a password or to add one or change one 
# input to detect the function of the program

while True:
        func = int(input("""
Press on one of the numbers below:
1. Show a saved Password.
2. Add a new Password.
3. Delete a saved Password.
4. Change a saved Password.
"""))
        #show a saved password
        def show_pass():
                database.SELpass(input("Enter The Url:\n"))
    
        #add a new password   
        def add_pass():
                database.INSpass(input("Enter The Url:\n"),input("Enter The Email:\n"),input("Enter The Password:\n"))
                print("Password saved successfully!")
    
        #Delete a saved password    
        def del_pass():
                database.DELpass(input("Enter The Email:\n"))
                print("Password deleted successfully!")

        #change a saved password
        def chg_pass():
                database.UPDpass(input("Enter The Email:\n"),input("Enter The New Password:\n"))
                print("Password changed successfully!")

        #detect a function 
        if func == 1:
                show_pass()
        elif func == 2:
                add_pass()
        elif func == 3:
                del_pass()
        elif func == 4:
                chg_pass()
        else:
                print("The number isn't correct")
        #return or close
        quits = input("Press c To Quit or another key to return: ")
        if quits == 'c':
                input("See You Again!")
                quit()