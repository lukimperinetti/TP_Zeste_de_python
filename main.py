#playeur_1 = input()
player_1 = input('Entrez le nom du 1er joueur : ').capitalize()
pv_player_1 = int(input('Et son nombre de PV : '))

player_2 = input('Entrez le nom du 2ème joueur : ').capitalize()
pv_player_2 = int(input('Et son nombre de PV : '))

init = "+ " + player_1 + " (" + str(pv_player_1) + ") affronte " + player_2 + " (" + str(pv_player_2) +")" + " +"

cadre = ""
for i in range(len(init)):
    cadre += '+'

print(cadre + '\n'+ init + '\n' + cadre)
