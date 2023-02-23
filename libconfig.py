import subprocess
import os

conf = "settings.conf"

def skipLines(file, howmuch):
    for i in range(howmuch):
        file.readline()

def readConfWordlist():
    conffile = open(conf)
    line = conffile.readline().replace("\n","")
    array = line.split("=")
    if array[1] != "" or array[1] != " " or array[1] != None:
        return array[1]

def readConfQuietMode():
    conffile = open(conf)
    skipLines(conffile, 1)
    line = conffile.readline().split("=")
    return line[1]

def readConfFile():
    conffile = open(conf)
    skipLines(conffile, 2)
    line = conffile.readline().replace("\n", "").split("=")
    return line[1]

def readConfAutoSet():
    conffile = open(conf)
    skipLines(conffile, 3)
    line = conffile.readline().replace("\n", "").split("=")
    return line[1]

def changeParameter(parameter, value):
    conffile = open(conf)
    line1 = conffile.readline().replace("\n","")
    line2 = conffile.readline().replace("\n","")
    line3 = conffile.readline().replace("\n","")
    line4 = conffile.readline().replace("\n","")
    if parameter == "wordlist":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
    elif parameter == "quietmode":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
    elif parameter == "file":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
    elif parameter == "autoset":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
