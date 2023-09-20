import csv, time, os, pathlib
from __init__ import platform


path = str(pathlib.Path(__file__).parent.resolve())
# print(os.path.abspath(__file__))


if platform == "darwin":
    path = path + "/"

    command_osx = '''
    echo "How many users would you want?"
    read users
    for i in $(seq $users)
    do
        echo ${x}
        osascript -e 'tell application "Terminal" to activate' \
        -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' \
        -e 'tell application "Terminal" to do script "python3 {y}meet.py" in selected tab of the front window'
        sleep 2

    done'''.format(x = r"{BASH_VERSION}", y = path)
    
    command = command_osx
    clearscreen = "clear"

elif platform == "win32" or platform == "win64":
    path = path + "\\"

    command_win32 = '''
    set /p asker="How many users would you want?: "
    for /l {x}x in (1,1,{y}sker%) DO (wt -w 0 nt cmd /k "python {z}meet.py" timeout /t 2 /nobreak > nul)'''.format(x = r"%%", y = r"%a", z = path)

    command = command_win32 #     @echo off, setlocal enableDelayedExpansion     For batch files
    clearscreen = "cls"

elif platform == "linux" or platform == "linux2":
    path = path + "/"

    command_linux = '''
    #!/bin/bash
    echo "How many users would you want?"
    read users
    for i in $(seq $users)
    do
        echo ${x}
        gnome-terminal --tab-with-profile=auto --title="tab$i" -e "python3 {y}meet.py"
        sleep 2

    done'''.format(x = r"{BASH_VERSION}", y = path)

    command = command_linux
    clearscreen = "clear"

else:
    exit("Not available yet.")



def names():
        
    names_file = path + "names.csv"
    if names_file.endswith("names.csv"):
        nameFile = open(names_file, "r")
        nameDict = csv.DictReader(nameFile, delimiter=',')
        nameList = []
        for row in nameDict:
            nameList.append(row)
        return(nameList)
    else:
        print("\nInvalid names file")
        time.sleep(1)
        os.system("clear")
        return names()


def details():

    details_file = path + "details.csv"
    if details_file.endswith("details.csv"):
        detailsFile = open(details_file, "r")
        detailsDict = csv.DictReader(detailsFile, delimiter=',')
        for row in detailsDict:
            detailsDict = row
        return detailsDict
    else:
        print("\nInvalid details file")
        time.sleep(1)
        os.system("clear")
        return details()

def get_link():
    os.system(f"{clearscreen}")
    url = input("Paste in your meeting link: ").strip()
    if url.startswith("https://meet.google.com/"):
        return url
    else:
        print("Invalid meeting link")
        time.sleep(1)
        return get_link()


def times():

    try:
        os.system(f"{command}")
    except ValueError:
        return times()


try:
    name = names()
    # detail = details()
except:
    print("Invalid files path")
    exit("Correct the file paths then run program again")

try:
    link = get_link()
except:
    exit()


if __name__ == "__main__":
    os.system(f"{clearscreen}")
    times()
    



