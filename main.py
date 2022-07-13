import sys
from func import *
import os
with open("settings.txt","r") as f:
    content=f.readlines()
    LANG = content[0].split(" = ")[1]
    NAME = content[1].split(" = ")[1].replace("\n","")
colored(150,150,150,["(c) - Arlequiin 2021 - 2022","(c) - Arlequiin 2021 - 2022"])
colored(50,150,180,["Hello {}. Language is set to {}\nYou can change it with 'setlang'\nType 'help' to show commands\n'end' to quit the program.".format(NAME,["english","french"][int(LANG)]),"Bonjour {}. La langue choisie est : {}\nSaisissez 'help' pour voir les commandes\n'end' pour mettre fin au programme.".format(NAME,["anglais","français"][int(LANG)])])
while True:
    with open("settings.txt","r") as f:
        content=f.readlines()
        LANG = content[0].split(" = ")[1]
        NAME = content[1].split(" = ")[1].replace("\n","")
    command=input("\033[1m\033[92m{}@calc:\033[94mucpv2\033[0m$ ".format(NAME))
    if command=="end":
        eval(command+"()")
    else:
        try:
         eval(command+"()")
        except:
         try:
            print(eval(command))
         except:
          colored(200,20,10,["/!\ Error /!\\nThis command doesn't exist\nType 'help' to show existing commands.","/!\ Erreur /!\\nCette commande n'existe pas\nEntrez 'help' pour voir les commandes qui existent."])

