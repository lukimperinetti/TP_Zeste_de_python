# -------- Initialize the data --------#
monsters = {
    'pythachu': {
        'name' : 'Pythachu',
        'attacks' : ['tonnerre', 'charge'],
    },
    'pythard': {
        'name' : 'Pytard',
        'attacks' : ['jet-de-flotte', 'charge'],
    },
    'ponytha': {
        'name' : 'Ponytha',
        'attacks' : ['brûlure', 'charge'],
    },
}

attacks = {
    'charge' : {'damages' : 20},
    'tonerre' : {'damages' : 50},
    'charge' : {'damages' : 40},
    'charge' : {'damages' : 40},
}

# create a list to store the players
players = []

# -------- Initialize the game --------#
def saisie_nom_et_pv(player_name):
    while True:
        nom = input(f'Entrez le nom du {player_name} joueur : ').capitalize()
        pv = input('Et son nombre de PV : ')
        if pv.isdigit() and int(pv) > 0:
            print('Monstres disponibles : ')
            for monster in monsters.values():
                print('- ', monster['name'])
            monster_name = input('Choisissez votre monstre : ').lower()
            if monster_name not in monsters.keys():
                print('Monstre invalide')            
            
            return nom, int(pv), monster_name
        else:
            print('Nombre de PV invalide (doit être un nombre positif)')
        
        


player_1, pv_1, monster_1 = saisie_nom_et_pv("1er")
dict_p_1 = {'name': player_1, 'pv': pv_1, 'monster': monster_1}
player_2, pv_2, monster_2 = saisie_nom_et_pv("2ème")
dict_p_2 = {'name': player_2, 'pv': pv_2, 'monster': monster_2}

players.append(dict_p_1)
players.append(dict_p_2)

print(players)

init = f"+ {player_1} ({pv_1}) affronte {player_2} ({pv_2}) +"
def afficher_cadre(texte):
    cadre = "+" * len(texte)
    print(f"{cadre}\n{texte}\n{cadre}\n\n")
afficher_cadre(init)


# -------- Choose your monster --------#




# -------- Round 1 Player 1 attack --------#

while int(pv_1) > 0 and int(pv_2) > 0:
    attack_names = ['charge', 'tonnerre']
    attack_damages = [20, 50]
    print(player_1 + ' Quelle attaque voulez-vous utiliser ? \n')
    i = 1
    for name in attack_names:
        print(i, name.capitalize(), -attack_damages[i - 1], ' PV')
        i += 1
    att1 = input('> ')
    while not att1.isdigit() or not 1 <= int(att1) <= len(attack_names):  # tant que mon input n'est pas un int, ou pas comprit entre 1 et le nombre d'index de attaque_name (on a nommé les choix 1 ou 2...)
        print('Attaque invalide, veuillez resaisir le numéro')
        att1 = input('> ')
    att1_idx = int(att1) - 1
    damages = attack_damages[att1_idx]
    action_p_1 = f"+ {player_1} attaque {player_2} qui perd {damages} PV +"
    pv_2 = int(pv_2 - damages)
    res_punch_p_1 = f"+ {player_2} a maintenant {pv_2} PV"
    afficher_cadre(action_p_1)
    afficher_cadre(res_punch_p_1)

    # -------- Round 1 Player 2 attack --------#

    if int(pv_2) > 0:
        print(player_2 + ' Quelle attaque voulez-vous utiliser ? \n')
        i = 1
        for name in attack_names:
            print(i, name.capitalize(), -attack_damages[i - 1], ' PV')
            i += 1
        att2 = input('> ')
        while not att2.isdigit() or not 1 <= int(att2) <= len(
                attack_names):  # tant que mon input n'est pas un int, ou pas comprit entre 1 et le nombre d'index de attaque_name (on a nommé les choix 1 ou 2...)
            print('Attaque invalide, veuillez resaisir le numéro')
            att2 = input('> ')
        att2_idx = int(att2) - 1
        damages2 = attack_damages[att2_idx]
        action_p_2 = f"+ {player_2} attaque {player_1} qui perd {str(damages2)} PV +"
        pv_1 = int(pv_1 - damages2)
        res_punch_p_2 = f"+ {player_1} a maintenant {str(pv_1)} PV+"
        afficher_cadre(action_p_2)
        afficher_cadre(res_punch_p_2)

    # -------- Round 1 result --------#

    if int(pv_1) <= 0 or int(pv_2) <= 0:
        print('La partie est terminée')
        result_line = "+ Résultat du combat : +"
        total_p_1 = f"+ {player_1} a {str(pv_1)} PV"
        total_p_2 = f"+ {player_2} a {str(pv_2)} PV"
        cadre_result = ""
        cadre_result = "+" * len(result_line)
        total_p_1 = f"+ {player_1} a {pv_1} PV".ljust(len(cadre_result) - 1, ' ') + "+" # ici une autre méthode pour créer le cadre sans avoir besoin de faire une fonction !
        total_p_2 = f"+ {player_2} a {pv_2} PV".ljust(len(cadre_result) - 1, ' ') + "+"
        print(cadre_result + '\n' + result_line + "\n" + total_p_1 + "\n" + total_p_2 + "\n" + cadre_result + '\n\n')
        break