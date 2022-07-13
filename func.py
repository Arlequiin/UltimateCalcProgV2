import sys
def colored(r, g, b, text):
    with open("settings.txt","r") as f:
        content=f.readlines()
        LANG = content[0].split(" = ")[1]
        NAME = content[1].split(" = ")[1].replace("\n","")
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text[int(LANG)]))
def colored2(r, g, b, text):
    return ("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))
def setlang():
    chosen = input(colored(1,1,1,["Choose between these language :\n1. English\n2. French\n>>> ","Choisissez parmi ces langages :\n1. Anglais\n2. Français\n>>> "]))
    LANG = str(int(chosen)-1)
    with open("settings.txt") as f:
        content=f.readlines()
    with open("settings.txt","w") as f2:
        for element in content:
            f2.write(element.replace(content[0],"LANG = "+LANG)+"\n")
    colored(50,10,120,["Language set to english","Langue sélectionnée : Français"])
def setname():
    chosen = input(colored(1,1,1,["What will be your new name ?\n>>> ","Quel sera votre nouveau nom ?\n>>> "]))
    NAME = chosen
    with open("settings.txt") as f:
        content=f.readlines()
    with open("settings.txt","w") as f2:
        for element in content:
            f2.write(element.replace(content[1],"NAME = "+NAME))
    colored(50,10,120,["Name set to "+NAME,"Nom choisi : "+NAME])
def help():
    colored(220,220,220,["'help' : Show commands\n'setlang' : Change language\n'setname' : Change name\nDiscord of the dev : Arlequiin#1853"])
def end():
    colored(255,0,0,["Finished the execution","Fin de l'exécution"])
    sys.exit()