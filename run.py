from __init__ import *
from random import randint
import csv




if platform == "darwin":
    path = runtime_path + "/"

    prompt_command = '''
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

elif platform == "win32" or platform == "win64":
    path = runtime_path + "\\"

    prompt_command = '''
    set /p asker="How many users would you want?: "
    for /l {x}x in (1,1,{y}sker%) DO (wt -w 0 nt cmd /k "python {z}meet.py" timeout /t 2 /nobreak > nul)'''.format(x = r"%%", y = r"%a", z = path)

   # @echo off, setlocal enableDelayedExpansion     For batch files

elif platform == "linux" or platform == "linux2":
    path = runtime_path + "/"

    prompt_command = '''
    #!/bin/bash
    echo "How many users would you want?"
    read users
    for i in $(seq $users)
    do
        echo ${x}
        gnome-terminal --tab-with-profile=auto --title="tab$i" -e "python3 {y}meet.psleep 2

    done'''.format(x = r"{BASH_VERSION}", y = path)

else:
    exit("Not available yet.")


def names():
    names_file = path + "names.csv"
    if names_file:
        nameList = []
        with open(names_file, "r") as nameFile:
            names_object = csv.reader(nameFile)
            for row in names_object:
                nameList.append(row)
        return "".join(nameList[randint(0, len(nameList))]).title()


def details():
    details_file = path + "details.csv"
    if details_file:
        with open(details_file, "r") as detailsFile:
            details_object = csv.DictReader(detailsFile, delimiter=',')
            for row in details_object:
                details_object = row
        return details_object["meetingLink"]


def times():
    try:
        os.system(prompt_command)
    except ValueError:
        return times()


try:
    name = names()
    url = details()
except:
    exit("Invalid files path")



if __name__ == "__main__":
    clean_up()
    clear(command=clear_arg)
    times()
    



