import os
cv = open("cv.txt", "r")
lv = os.system("curl https://cdn.jonesserver.online/lv.txt")


if cv != lv:
    print("updates needed")
else:
    print("no updates needed")