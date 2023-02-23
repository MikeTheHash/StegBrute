import subprocess
import argparse
import colorama
import libconfig
import banner
import loglib

banner.banner()
print("       By MikeTheHash                             https://github.com/MikeTheHash")
print("                                                             SteghideBrute v1.0\n")
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="set the file to bruteforce")
parser.add_argument("--wordlist", help="set your wordlist")
parser.add_argument("--set", help="auto setting with settings.conf")
args = parser.parse_args()
autoset = bool(args.set)
file = str(args.file)
pwd = subprocess.getoutput("pwd")

'''
existenceAutoSet = libconfig.readConfAutoSet()
if bool(args.set) == True:
    libconfig.changeParameter("autoset", "true")
    if existenceAutoSet == "true" and args.set == None:
        global existenceWLConf
        existenceWLConf = libconfig.readConfWordlist()
    elif existenceWLConf != None and args.wordlist == None or args.wordlist == "":
        global wordlist_arg
        wordlist_arg = libconfig.readConfWordlist()
    else:
        wordlist_arg = str(args.wordlist)
else:
    libconfig.changeParameter("autoset", "false")'''

wordlist_arg = str(args.wordlist)
wordlist = open(wordlist_arg)

numlines = subprocess.getoutput(f"wc -l {wordlist_arg}").split(" ")
print("**********************************")
print("Passwords: " + str(numlines[0]) + "\nHex: " + hex(int(numlines[0]))) 
print("**********************************")

for line in wordlist:
    found = False
    passwd = wordlist.readline().replace("\n","")
    output = subprocess.getoutput(f"steghide extract -sf {file} -p {passwd}")
    if "wrote extracted data to" in output:
        print("****************************")
        print(f"{colorama.Fore.WHITE}[{colorama.Fore.BLUE}+{colorama.Fore.WHITE}]{colorama.Fore.RED} ACCESS GRANTED {colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.WHITE}[{colorama.Fore.RED}!{colorama.Fore.WHITE}]{colorama.Style.RESET_ALL} Password Found: " + colorama.Fore.RED + passwd + colorama.Style.RESET_ALL + f"\nFile: {file}")
        print(f"File extracted on: {pwd}")
        loglib.createLogs(f"Password Found: {passwd} ~ File: {file}")
        found = True
    elif "the file" in output and "does already exist." in output:
        print(f"{colorama.Fore.WHITE}[{colorama.Fore.RED}-{colorama.Fore.WHITE}] {colorama.Style.RESET_ALL}{colorama.Back.RED}{colorama.Fore.WHITE}The file already exist{colorama.Style.RESET_ALL}")
        loglib.createLogs(f"File already exist")
        break
    elif "is not supported." in output:
        print(f"{colorama.Fore.WHITE}[{colorama.Fore.RED}-{colorama.Fore.WHITE}] {colorama.Style.RESET_ALL}{colorama.Back.RED}{colorama.Fore.WHITE}The format of the file is not supported{colorama.Style.RESET_ALL}")
        break
    else:
        print(f"{colorama.Fore.WHITE}[{colorama.Fore.RED}+{colorama.Fore.WHITE}]{colorama.Style.RESET_ALL} Trying {passwd} | Access Denied")
    if found == True:
        break