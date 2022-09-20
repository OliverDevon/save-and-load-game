import os
import time

name = "Oliver"
name2 = "Todd"

def save(num):
    if num == 1:
        list = [
            name
        ]
        for items in list:
            with open("save1", "w") as save1:
                save1.write(items+"\n")
    if num == 2:
        list = [
            name
        ]
        for items in list:
            with open("save2", "w") as save2:
                save2.write(items+"\n")

def load(loadNum):
    if loadNum == 1:
        with open("save1", "r") as load1:
            loadedName= load1.readlines()
            name = loadedName[0][:-1]
            return name
    if loadNum == 2:
        with open("save2", "r") as load2:
            loadedName= load2.readlines()
            name2 = loadedName[0][:-1]
            return name2

try:
    save(1)
    print(load(1))
    
except OSError:
    print("can't find file / can't save file")
