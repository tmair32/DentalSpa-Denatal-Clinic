import os
from os import rename
import sys
sys.stdin = open("1460.txt", "rt", encoding="UTF8")

dir_url = "/Users/jae/Desktop/덴탈스파/1460/"
files = os.listdir(dir_url)

person = []
for i in range(219):
    person.append(input())

num = 0
for file in files:
    print(file, "=>", person[num])
    if file == "rename.py":
        continue
    else:
        rename(dir_url+file, dir_url+person[num]+".pdf")
    num += 1
