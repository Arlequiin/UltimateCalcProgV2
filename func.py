import sys
import random
def is_float(number):
    try:
        (float(number))
        return True
    except:
        return False
def colored(r, g, b, text):
    with open("settings.txt","r") as f:
        content=f.readlines()
        LANG = content[0].split(" = ")[1]
        NAME = content[1].split(" = ")[1].replace("\n","")
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text[int(LANG)]))
def colored2(r, g, b, text):
    return ("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))
def setlang():
    colored(1,1,1,["Choose between these language :\n1. English\n2. French\n","Choisissez parmi ces langages :\n1. Anglais\n2. Français\n"])
    chosen = input(colored2(1,1,1,">>> "))
    LANG = str(int(chosen)-1)
    with open("settings.txt") as f:
        content=f.readlines()
    with open("settings.txt","w") as f2:
        for element in content:
            f2.write(element.replace(content[0],"LANG = "+LANG)+"\n")
    colored(50,10,120,["Language set to english","Langue sélectionnée : Français"])
def setname():
    colored(1,1,1,["What will be your new name ?","Quel sera votre nouveau nom ?"])
    chosen = input(colored2(1,1,1,">>> "))
    NAME = chosen
    with open("settings.txt") as f:
        content=f.readlines()
    with open("settings.txt","w") as f2:
        for element in content:
            f2.write(element.replace(content[1],"NAME = "+NAME+'\n'))
    colored(50,10,120,["Name set to "+NAME,"Nom choisi : "+NAME])
def setcalc():
    colored(1,1,1,["What calculator you have","Quel calculatrice vous avez ? ?"])
    chosen = input(colored2(1,1,1,">>> "))
    CALC = chosen
    with open("settings.txt") as f:
        content=f.readlines()
    with open("settings.txt","w") as f2:
        for element in content:
            f2.write(element.replace(content[2],"CALC = "+CALC))
    colored(50,10,120,["Name set to "+CALC,"Nom choisi : "+CALC])
def showhelp():
    colored(0,255,220,["'showhelp' : Show commands\n'setlang' : Change language\n'setname' : Change name\n'ruleof3' : calculate unknown with rule of 3\nrand: random choice\nDiscord of the dev : Arlequiin#1853","'showhelp' : Affiche les commandes\n'setlang' : permet de changer la langue\n'setname' : permet de changer le nom\n'ruleof3' permet de calculer l'inconnu avec la règle de trois\n'rand' permet de faire un choix aléatoire\nDiscord du dev : Arlequiin#1853"])
def end():
    colored(255,0,0,["Finished the execution","Fin de l'exécution"])
    sys.exit()
def rand():
    colored(150,30,60,["Enter two or more elements, one of them will be randomly picked.","Entrez deux éléments ou plus, l'un d'entre eux sera choisi aléatoirement."])
    text = input(colored2(150,30,60,">>> "))
    print(random.choice(text.split(",")))
def ruleof3():
    colored(200,220,220,["First of all you have to give symbols, or names to the tree elements then their values","Premièrement, veuillez renseigner les symboles/noms des trois éléments et leurs valeurs."])
    d = {}
    db = {}
    countnotint = 0
    for i in range(3):
        a = input(colored2(150,150,150,"Name : "))
        colored(30,255,100,["Put sorted element, for instance v then d then t for v=d/t","Mettez les éléments en ordre, exemple v puis d puis t pour v=d/t"])
        colored(255,0,255,["Just put a letter for the unknown value","Mettez une lettre pour la valeur inconnue."])
        colored(80,100,0,["What is the value of {}?".format(a),"Quelle est la valeur de {}?".format(a)])
        b = input(colored2(150,150,150,"Value of {} : ".format(a)))
        if is_float(b) == False:
            pass
            colored(1,1,1,[b+" is unknown",b+" est inconnu"])
            unknown = b
            unknown2 = a
            countnotint+=1
        else:
            b=float(b)
            db[a] = b
        d[a] = b
    if countnotint!=1:
        colored(255,0,0,["/!\ Unexpected error /!\ \nThere is more that one unknown value or no unknown number","/!\ Erreur /!\ \n Il y a plus d'une valeur inconnue ou pas d'inconnu."])
    else:
      db2 = {}
      for w in sorted(db, key=db.get, reverse=True):
       db2[w] = db[w]
      d0 = list(d.keys())
      d0.append(unknown2)
      d2 = {d0[0]:'{}/{}'.format(d0[1],d0[2]),d0[1]:'{}*{}'.format(d0[0],d0[2]),d0[2]:'{}/{}'.format(d0[0],d0[1])}
      d3 = {d0[0]:'{}/{}'.format(d[d0[1]],d[d0[2]]),d0[1]:'{}*{}'.format(d[d0[0]],d[d0[2]]),d0[2]:'{}/{}'.format(d[d0[1]],d[d0[0]])}
      print("{} = {}".format(list(d2.keys())[0],list(d2.values())[0]))
      for i in range(3):
        if d0[i] == unknown2:
         print("{} = {}".format(list(d2.keys())[i],list(d2.values())[i]))
         print("{} = {}".format(list(d2.keys())[i],list(d3.values())[i]))
         print("{} = {}".format(list(d2.keys())[i],eval(list(d3.values())[i])))
'''
3 = 6/2
6 = 3*2
2 = 6/3
'''