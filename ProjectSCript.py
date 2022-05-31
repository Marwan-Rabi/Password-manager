#choose between (preview a password or add a new password )
#if he choose to add new pw then give hem an input to add a username and password and url
#save this pw as a dictionary (key and password)
#preview this pw
#else if he choose to previw to pw then give him an input to choose a url (as a key)
#preview it


print("Hello, In the password manager")
start = int(input("Click 1 to add a new Password or\nclick 2 to previw a password")) 
if start == 1:
    #Information inputs
    url = input("Add the Website url")
    userName = input("Add the username")
    passWord = input("Add the password")
    #save the inputs
    PassWordFile = open(f"E:\Marwan\PROGRAMMING\py projects\Password maneger\{url}.txt", "a")
      
    userNam = str(f" url:{url} \n username: {userName}\n password: {passWord}")    
    PassWordFile.write(userNam)
else:
    #preview this pw
    preview = input("Enter the url of the pass word")
    with open(rf"E:\Marwan\PROGRAMMING\py projects\Password maneger\{preview}.txt", "r") as file:
        #preview it
        PassWordFil = file.read()
        if preview in PassWordFil:
            print( PassWordFil)
        else: 
            print("Non Exist password")
input("Press any key to exit") 
quit()           
        
    
