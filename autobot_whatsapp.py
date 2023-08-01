'''
Author : Syed Zulqarnain Haider

Program : Automatic Whatsapp Messenger

Version : 1.0.0

Country : Pakistan

Programming Language : Python
'''
import os, pywhatkit

#Folder Checking
dirs = os.system("ls")
dirFound = False
for dir in str(dirs):
    if str(dir) == "essentials":
        dirFound = True
        break
if not dirFound:
    os.system("mkdir essentials")
    
folder = "./essentials"
#File Checking
try:
    __f1 = open(folder+"/knownContacts.txt","r")
except FileNotFoundError:
    __f1 = open(folder+"/knownContacts.txt","w")
__f1.close()

#File Checking
try:
    __f2 = open(folder+"/unknownContacts.txt","r")
except FileNotFoundError:
    __f2 = open(folder+"/unknownContacts.txt","w")
__f2.close()

#This Function removes \n from string
def remLine(string):
    return string[:len(string)-1]

#This Function returns Known Contacts
def getKnownContacts():
    global folder
    try:
        f = open(folder+"/knownContacts.txt","r")
        known = []
        for each in f:
            known.append(remLine(each))
        f.close()
        return known
    except FileNotFoundError:
        print("Known Contacts File Not Found!")
        input()
        
def setKnownContacts(known):
    global folder
    try:
        f = open(folder+"/knownContacts.txt","w")
        if len(known) > 0:
            for i in known:
                f.write(i+"\n")
        f.close()
        return
    except FileNotFoundError:
        print("Known Contacts File Not Found!")
        input()
        
# Setting Unknown Contacts
def setUnknownContacts(unknown):
    global folder
    try:
        f = open(folder+"/unknownContacts.txt","w")
        if len(unknown) > 0:
            for i in unknown:
                f.write(i+"\n")
        f.close()
        return
    except FileNotFoundError:
        print("Unknown Contacts File Not Found!")
        input()
    
#This Function returns Unknown Contacts
def getUnknownContacts():
    global folder
    try:
        f = open(folder+"/unknownContacts.txt","r")
        unknown = []
        for each in f:
            unknown.append(remLine(each))
        f.close()
        return unknown
    except FileNotFoundError:
        print("Unknown Contacts File Not Found!")
        input()
        
   
#Clears Screen
def clrscr():
    os.system("cls")
    
#Menu Method
def menu():
    choice = 0
    while True:
        clrscr()
        print("Select the option.\n\n")
        print("1. Add Numbers")
        print("2. Remove Numbers")
        print("3. View Numbers")
        print("4. Initiate Procedure")
        print("\n5. Save and Exit")
        choice = getValidInput()
        if choice == 1:
            addNumbers()
        elif choice == 2:
            removeNumbers()
        elif choice == 3:
            viewNumbers()
        elif choice == 4:
            initiate()
        elif choice == 5:
            break
        else:
            continue
        
        
#Adding Numbers
def addNumbers():
   choice = 0
   while True:
       clrscr()
       print("Select Contact Type to add numbers to.\n\n")
       print("1. Known Contacts")
       print("2. Unknown Contacts")
       print("\n3. Back")
       choice = getValidInput()
       if choice == 1:
           c = 0
           j = 0
           list = getKnownContacts()
           tempList = []
           while True:
               clrscr()
               if len(tempList) > 0:
                   k = 1
                   for i in tempList:
                       print(str(k)+". "+i)
                       k+=1
               num = input("\n\nEnter Valid Contact >> ")
               nums = num[1:]
               if num == "":
                   clrscr()
                   if len(tempList) > 0:
                       list = list + tempList
                       setKnownContacts(list)
                   break
               elif len(num) < 13:
                   clrscr()
                   print("Contact Length is too Short!")
                   input()
                   continue
               elif num[0] != "+":
                   clrscr()
                   print("Please Enter Country Code First!")
                   input()
                   continue
               elif tempList.count(num) > 0 or list.count(num) > 0:
                   clrscr()
                   print("This Contact Already Exists!")
                   input()
                   continue
               elif not nums.isnumeric():
                   clrscr()
                   print("Please Enter a valid Contact Number!")
                   input()
                   continue
               else:
                   tempList.append(num)
                   j += 1
           
       elif choice == 2:
           c = 0
           j = 0
           list = getUnknownContacts()
           tempList = []
           while True:
               clrscr()
               if len(tempList) > 0:
                   k = 1
                   for i in tempList:
                       print(str(k)+". "+i)
                       k += 1
               num = input("\n\nEnter Valid Contact >> ")
               nums = num[1:]
               if num == "":
                   clrscr()
                   if len(tempList) > 0:
                       list = list + tempList
                       setUnknownContacts(list)
                   break
               elif len(num) < 13:
                   clrscr()
                   print("Contact Length is too Short!")
                   input()
                   continue
               elif num[0] != "+":
                   clrscr()
                   print("Please Enter Country Code First!")
                   input()
                   continue
               elif tempList.count(num) > 0 or list.count(num) > 0:
                   clrscr()
                   print("This Contact Already Exists!")
                   input()
                   continue
               elif not nums.isnumeric():
                   clrscr()
                   print("Please Enter a valid Contact Number!")
                   input()
                   continue
               else:
                   tempList.append(num)
                   j += 1
           
       elif choice == 3:
           break
       else:
           clrscr()
           print("Please Enter Valid Input!")
           input()
           continue
       
   
#Removing Numbers
def removeNumbers():
    choice = 0
    while True:
        clrscr()
        print("Select Contact Type to remove numbers from.\n\n")
        print("1. Known Contacts")
        print("2. Unknown Contacts")
        print("\n3. Back")
        choice = getValidInput()
        if choice == 1:
            known = getKnownContacts()
            if len(known) > 0:
                c = 0
                while True:
                    j = 1
                    clrscr()
                    print("==> Known Contacts\n")
                    print("Select Contact to Remove.(*Press Enter to go Back)\n\n")
                    for i in known:
                        print(str(j)+". "+ i)
                        j += 1
                    c = getValidInput()
                    if c == -1:
                        break
                    if c < 1 or c >= j:
                        clrscr()
                        print("Please Enter Valid Option Number")
                        input()
                        continue
                    else:
                        known.remove(known[c-1])
                        setKnownContacts(known)
                        known = getKnownContacts()
                        j = 1
            else:
                 clrscr()
                 print("Please Add Numbers First!")
                 input()
                 continue
        elif choice == 2:
            unknown = getUnknownContacts()
            if len(unknown) > 0:
                c = 0
                while True:
                    j = 1
                    clrscr()
                    print("==> Unknown Contacts\n")
                    print("Select Contact to Remove.(*Press Enter to go Back)\n\n")
                    for i in unknown:
                        print(str(j)+". "+ i)
                        j += 1
                    c = getValidInput()
                    if c == -1:
                        break
                    if c < 1 or c >= j:
                        clrscr()
                        print("Please Enter Valid Option Number")
                        input()
                        continue
                    else:
                        unknown.remove(unknown[c-1])
                        setUnknownContacts(unknown)
                        unknown = getUnknownContacts()
                        j = 1
            else:
                 clrscr()
                 print("Please Add Numbers First!")
                 input()
                 continue
        elif choice == 3:
            break
        else:
            clrscr()
            print("Please Enter Valid Input")
            input()
            continue
                        
                            
#View Contacts
def viewNumbers():
    known = getKnownContacts()
    unknown = getUnknownContacts()
    
    clrscr()
    print("\n=> Known Contacts :--\n")
    if len(known) > 0:
        j = 1
        for i in known:
            print(str(j)+". "+ i)
            j += 1
    else:
        print("Known Contact List is Empty")
    
    print("\n=> Unknown Contacts :--\n")
    if len(unknown) > 0:
        j = 1
        for i in unknown:
            print(str(j)+". "+ i)
            j += 1
    else:
        print("Unknown Contact List is Empty")
    input()

#Initiating Procedure
def initiate():
    waitTime = 7
    tabCloses = True
    closeTime = 5

    unknown = getUnknownContacts()
    known = getKnownContacts()

    if unknown == None or known == None:
        clrscr()
        print("There is some problem while getting data from Files!")
        input()
        return
    elif len(known) < 1:
        clrscr()
        print("Known Contacts list is Empty!")
        print("Please enter some known contacts first to continue the process.")
        input()
        return
    elif len(unknown) < 1:
        clrscr()
        print("Unknown Contact List is Empty.")
        print("Please enter some unknown contacts first to continue the process.")
        input()
        return
    
    clrscr()
    msg = str(input("Enter Message : "))
    

    i = 1
    j = 1
    k = len(known) + len(unknown)
    progress = 0
    for m in unknown:
        pywhatkit.sendwhatmsg_instantly(m,msg,waitTime,tabCloses,closeTime)
        progress += 1
        i+=1
        clrscr()
        print("Process -> ("+str(progress)+"/"+str(k)+")")
        if i == 10:
            i = 1
            for n in known:
                pywhatkit.sendwhatmsg_instantly(n,msg,waitTime,tabCloses,closeTime)
                progress += 1
                j+=1
                clrscr()
                print("Process -> ("+str(progress)+"/"+str(k)+")")
                if j == 3:
                    j = 1
                    break

    clrscr()
    print("Procedure Completed!")
    input()
    
def getValidInput():
    
    try:
       
       
       choice = input("Type Here : ")
       if choice == "":
           return -1
       choice = int(choice)
    except ValueError:
       clrscr()
       print("Please enter valid option number.")
       input()
       return 0
    return choice
       
#Main Method     
def main():
    menu()
    clrscr()
    print("✓ All Files are Saved.")
    print("Program Finished!")
    
    
if __name__ == '__main__':
    main()
