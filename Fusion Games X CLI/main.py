#start CLI backend

import os #command runner

#run command: os.system("ls -l")


def get():
    q1 = str(input("Branch? (case sensitive)"))
    Main = "main", "Main"
    Hosting = "Hosting", "Host", "hostingproviders"
    if q1 == Main:
        print("Cloning from main branch.")
        os.system("git clone -b main https://gitlab.com/fusiongames1/fusio-games-x.git")
    elif q1 == Hosting:
        print("Cloning hosting branch. (for hosting locally)")
        os.system("git clone -b hostingproviders https://gitlab.com/fusiongames1/fusion-games-x.git")

def update():
    cv = open("cv.txt", "r")
    lv = open("https://cdn.jonesserver.online/lv.txt", "r")
    print("Checking for updates.")
    if cv != lv:
        print("Updates needed.")
        os.system("git pull")
    else:
        print("No updates needed.")

update()