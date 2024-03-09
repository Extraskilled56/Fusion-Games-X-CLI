#start CLI backend

import os #command runner

#run command: os.system("ls -l")


def get():
    q1 = str(input("Branch? (case sensitive)"))
    Main = "main", "Main"
    Hosting = "Hosting", "Host", "hostingproviders"
    if q1 == Main:
        print("cloning from main branch.")
        os.system("git clone -b main https://gitlab.com/fusiongames1/fusio-games-x.git")
    elif q1 == Hosting:
        print("cloning hosting branch (for hosting locally)")
        os.system("git clone -b hostingproviders https://gitlab.com/fusiongames1/fusion-games-x.git")

def update():
    