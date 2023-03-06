import subprocess
import os

conf = "../settings.conf"

def skipLines(file, howmuch):
    for i in range(howmuch):
        file.readline()

def read(parameter):
    if parameter == "wordlist":
        conffile = open(conf)
        line = conffile.readline().replace("\n","")
        array = line.split("=")
        if array[1] != "" or array[1] != " " or array[1] != None:
            return array[1]
    elif parameter == "quietmode":
        conffile = open(conf)
        skipLines(conffile, 1)
        line = conffile.readline().split("=")
        return line[1]
    elif parameter == "file":
        conffile = open(conf)
        skipLines(conffile, 2)
        line = conffile.readline().replace("\n", "").split("=")
        return line[1]
    elif parameter == "autoset":
        conffile = open(conf)
        skipLines(conffile, 3)
        line = conffile.readline().replace("\n", "").split("=")
        return line[1]
    elif parameter == "savelogs":
        conffile = open(conf)
        skipLines(conffile, 4)
        line = conffile.readline().replace("\n", "").split("=")
        return line[1]
    elif parameter == "interface":
        conffile = open(conf)
        skipLines(conffile, 5)
        line = conffile.readline().replace("\n", "").split("=")
        return line[1]

def setParameter(parameter, value):
    conffile = open(conf)
    line1 = conffile.readline().replace("\n","")
    line2 = conffile.readline().replace("\n","")
    line3 = conffile.readline().replace("\n","")
    line4 = conffile.readline().replace("\n","")
    line5 = conffile.readline().replace("\n","")
    if parameter == "wordlist":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
        os.system(f"echo \"{line5}\" >> settings.conf")
    elif parameter == "quietmode":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
        os.system(f"echo \"{line5}\" >> settings.conf")
    elif parameter == "file":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
        os.system(f"echo \"{line5}\" >> settings.conf")
    elif parameter == "autoset":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
        os.system(f"echo \"{line5}\" >> settings.conf")
    elif parameter == "savelogs":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")
    elif parameter == "interface":
        conffile = open(conf)
        os.system("rm settings.conf")
        os.system("touch settings.conf")
        os.system(f"echo \"{line1}\" >> settings.conf")
        os.system(f"echo \"{line2}\" >> settings.conf")
        os.system(f"echo \"{line3}\" >> settings.conf")
        os.system(f"echo \"{line4}\" >> settings.conf")
        os.system(f"echo \"{line5}\" >> settings.conf")
        os.system(f"echo \"{parameter}={value}\" >> settings.conf")

