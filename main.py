# -------- Initialize the game --------#

player_1 = input('Entrez le nom du 1er joueur : ').capitalize()
pv_player_1 = input('Et son nombre de PV : ')
while not pv_player_1.isdigit():
    print('Nombre de PV invalide (doit être un nombre positif)')
    pv_player_1 = input('Entrez à nouveau : ')
pv_1 = int(pv_player_1)

player_2 = input('Entrez le nom du 2ème joueur : ').capitalize()
pv_player_2 = input('Et son nombre de PV : ')
while not pv_player_2.isdigit():
    print('Nombre de PV invalide (doit être un nombre positif)')
    pv_player_2 = input('Entrez à nouveau : ')
pv_2 = int(pv_player_2)

init = "+ " + player_1 + " (" + str(pv_1) + ") affronte " + player_2 + " (" + str(pv_2) + ")" + " +"


# TODO: create a function to do that cadre to call it everywhere !
cadre = ""
for i in range(len(init)):
    cadre += '+'
print(cadre + '\n' + init + '\n' + cadre + '\n\n')

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
    while not att1.isdigit() or not 1 <= int(att1) <= len(attack_names) : # tant que mon input n'est pas un int, ou pas comprit entre 1 et le nombre d'index de attaque_name (on a nommé les choix 1 ou 2...)
        print('Attaque invalide, veuillez resaisir le numéro')
        att1 = input('> ')

    att1_idx = int(att1) - 1
    damages = attack_damages[att1_idx]

    action_p_1 = "+ " + player_1 + " attaque " + player_2 + " qui perd " + str(damages) + " PV" + " +"
    pv_2 = int(pv_2 - damages)
    res_punch_p_1 = "+ " + player_2 + " a maintenant " + str(pv_2) + " PV"
    cadre2 = ""
    for i in range(len(action_p_1)):
        cadre2 += '+'
    calc = len(cadre2) - len(res_punch_p_1)
    res_punch_p_1 = res_punch_p_1.ljust(len(res_punch_p_1) + calc - 1, ' ') + "+"
    print(cadre2 + '\n' + action_p_1 + "\n" + res_punch_p_1 + "\n" + cadre2 + '\n\n')

    # -------- Round 1 Player 2 attack --------#

    if int(pv_2) > 0:
        print(player_2 + ' Quelle attaque voulez-vous utiliser ? \n')

        i = 1

        for name in attack_names:
            print(i, name.capitalize(), -attack_damages[i - 1], ' PV')
            i += 1

        att2 = input('> ')
        while not att2.isdigit() or not 1 <= int(att2) <= len(attack_names) : # tant que mon input n'est pas un int, ou pas comprit entre 1 et le nombre d'index de attaque_name (on a nommé les choix 1 ou 2...)
            print('Attaque invalide, veuillez resaisir le numéro')
            att2 = input('> ')

        att2_idx = int(att2) - 1
        damages2 = attack_damages[att2_idx]

        action_p_2 = "+ " + player_2 + " attaque " + player_1 + " qui perd " + str(damages2) + " PV" + " +"
        pv_1 = int(pv_1 - damages2)
        res_punch_p_2 = "+ " + player_1 + " a maintenant " + str(pv_1) + " PV"
        cadre2 = ""
        for i in range(len(action_p_2)):
            cadre2 += '+'
        calc = len(cadre2) - len(res_punch_p_2)
        res_punch_p_2 = res_punch_p_2.ljust(len(res_punch_p_2) + calc - 1, ' ') + "+"
        print(cadre2 + '\n' + action_p_2 + "\n" + res_punch_p_2 + "\n" + cadre2 + '\n\n')

    # -------- Round 1 result --------#
    if int(pv_1) <= 0 or int(pv_2) <= 0:
        print('La partie est terminée')

        result_line = "+ Résultat du combat : +"
        total_p_1 = "+ " + player_1 + " a " + str(pv_1) + " PV"
        total_p_2 = "+ " + player_2 + " a " + str(pv_2) + " PV"
        cadre_result = ""
        for i in range(len(result_line)):
            cadre_result += '+'
        calc_line_p_1 = len(cadre_result) - len(total_p_1)
        total_p_1 = total_p_1.ljust(len(total_p_1) + calc_line_p_1 - 1, ' ') + "+"
        calc_line_p_2 = len(cadre_result) - len(total_p_2)
        total_p_2 = total_p_2.ljust(len(total_p_2) + calc_line_p_2 - 1, ' ') + "+"
        print(cadre_result + '\n' + result_line + "\n" + total_p_1 + "\n" + total_p_2 + "\n" + cadre_result + '\n\n')
        break
