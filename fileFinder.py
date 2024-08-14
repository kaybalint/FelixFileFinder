import zipfile
from zipfile import ZipFile
import pyfiglet

BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
ENDC = "\033[0m"


felixFischoeder = open('felix 1.txt').read()
print(felixFischoeder)
ascii_banner = pyfiglet.figlet_format("foxy felixs file finder!")
print(ascii_banner)


keyWordsList = ["password","token","admin","username","secret","accesskey","secretkey","pwd"]
fileEndings = ["txt","html","config","cshtml","xml","aspx"]

def oneFile(userFile):
    with ZipFile(userFile, 'r') as zip: 
        fileNames = zip.namelist()
        for items in range (0,len(fileNames)):
            try:
                y = fileNames[items].split(".")[1]
            except:
                pass
            if y in fileEndings:
                with zip.open(fileNames[items]) as myfile:
                    file_data = myfile.readlines()
                    
                    for x in range(len(file_data)):
                        try:
                            line = str(file_data[x].decode("UTF-8"))
                            line= line.strip()
                        except:
                            pass
                        
                        for keyWord in keyWords:
                        
                            if keyWord in line.lower():
                                if keyWord in ["admin","pwd","secret","password"]:
                                    print(f"found {RED}{keyWord}{ENDC} on line {x+1} in file, {myfile.name}")
                                    print(line +"\n")
                                else:
                                    print(f" found {BLUE}{keyWord}{ENDC} on line {x+1} in file, {myfile.name}")
                                    print(line +"\n")
                                
                            else:
                                continue
                            
def multipleFiles():
    fileList = []
    x = "True"
    print("Enter the file names, one by one [press Enter], once finished enter DONE.")
    while( x == "True"):
        userFiles = input("Enter file name: ")
        if userFiles == "DONE":
            x = False
        if not userFiles.endswith(".zip") or userFiles == "DONE":
            print("Invalid file.")
            continue
        fileList.append(userFiles)
    for items in range(0,len(fileList)):
        oneFile(fileList[items])
  
userInput = input("Do you want to open one file or multiple? Enter one or multiple: ")
keyWords = open("keyWords.txt").read().splitlines()
fileEndings = open("fileEndings.txt").read().splitlines()


userKeyWords = input(f"This the current list of key words being searched: \n{keyWords}\nDo you want to add anymore to the list? [YES/NO] ")
if userKeyWords == "YES":
    new_keyWords = open("keyWords.txt","a")
    z = "True"
    print("Enter the key words, one by one [press Enter], once finished enter DONE.\n")
    while(z == "True"):
        words = input("Enter the keyword: ")
        if words == "DONE":
            z = False
            continue
        new_keyWords.write(words+"\n")
    new_keyWords.close()
elif userKeyWords == "NO":
    next
else:
    print("Invalid input.")


userFileEndings = input(f"\nThis the current list of file endings being searched: \n{fileEndings}\nDo you want to add anymore to the list? [YES/NO] ")
if userFileEndings == "YES":
    new_FileEndings = open("FileEndings.txt","a")
    a = "True"
    print("Enter the key words, one by one [press Enter], once finished enter DONE.\n")
    while(a == "True"):
        new_userFileEndings = input("Enter the keyword: ")
        if new_userFileEndings == "DONE":
            a = False
            continue
        new_FileEndings.write(new_userFileEndings+"\n")
        fileEndings.append(new_userFileEndings)
    new_FileEndings.close()
elif userFileEndings == "NO":
    next
else:
    print("Invalid input.")



if userInput.lower() == "one":
    userFile = input("Enter the file name: ")
    oneFile(userFile)
elif userInput.lower() == "multiple":
    multipleFiles()
else:
    print("You didn't put the correct input in.")
