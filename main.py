# -------- Initialize the game --------#

player_1 = input('Entrez le nom du 1er joueur : ').capitalize()
pv_player_1 = int(input('Et son nombre de PV : '))
player_2 = input('Entrez le nom du 2ème joueur : ').capitalize()
pv_player_2 = int(input('Et son nombre de PV : '))
init = "+ " + player_1 + " (" + str(pv_player_1) + ") affronte " + player_2 + " (" + str(pv_player_2) + ")" + " +"
cadre = ""
for i in range(len(init)):
    cadre += '+'
print(cadre + '\n' + init + '\n' + cadre + '\n\n')

# -------- Round 1 Player 1 attack --------#

print('Quelle attaque voulez-vous utiliser ? \n')
punch_p_1 = input('1. Charge (-20 PV)\n2. Tonnerre (-50 PV)')

punch_power = 0

if punch_p_1 == 1 or 'Charge' :
    punch_power = 20
elif punch_p_1 == 2 or 'Tonnerre':
    punch_power = 50
else:
    print("Désolé mais ce que tu dis n'a aucun sens...")
action_p_1 = "+ " + player_1 + " attaque " + player_2 + " qui perd " + str(punch_power) + " PV" + " +"
player_2_new_hp = str(pv_player_2 - punch_power)
res_punch_p_1 = "+ " + player_2 + " a maintenant " + str(player_2_new_hp) + " PV"
cadre2 = ""
for i in range(len(action_p_1)):
    cadre2 += '+'
calc = len(cadre2) - len(res_punch_p_1)
res_punch_p_1 = res_punch_p_1.ljust(len(res_punch_p_1) + calc - 1, ' ') + "+"
print(cadre2 + '\n' + action_p_1 + "\n" + res_punch_p_1 + "\n" + cadre2 + '\n\n')

# -------- Round 1 Player 2 attack --------#

print('Quelle attaque voulez-vous utiliser ? \n')
punch_p_1 = input('1. Charge (-20 PV)\n2. Tonnerre (-50 PV)')

punch_power = 0

if punch_p_2 == 1 or 'Charge' :
    punch_power = 20
elif punch_p_2 == 2 or 'Tonnerre':
    punch_power = 50
else:
    print("Désolé mais ce que tu dis n'a aucun sens...")

action_p_2 = "+ " + player_2 + " attaque " + player_1 + " qui perd " + str(punch_power) + " PV" + " +"
player_1_new_hp = str(pv_player_1 - punch_power)
res_punch_p_2 = "+ " + player_1 + " a maintenant " + str(player_1_new_hp) + " PV"
cadre2 = ""
for i in range(len(action_p_2)):
    cadre2 += '+'
calc = len(cadre2) - len(res_punch_p_2)
res_punch_p_2 = res_punch_p_2.ljust(len(res_punch_p_2) + calc - 1, ' ') + "+"
print(cadre2 + '\n' + action_p_2 + "\n" + res_punch_p_2 + "\n" + cadre2 + '\n\n')

# -------- Round 1 result --------#

result_line = "+ Résultat du combat : +"
total_p_1 = "+ " + player_1 + " a " + str(player_1_new_hp) + " PV"
total_p_2 = "+ " + player_2 + " a " + str(player_2_new_hp) + " PV"
cadre_result = ""
for i in range(len(result_line)):
    cadre_result += '+'
calc_line_p_1 = len(cadre_result) - len(total_p_1)
total_p_1 = total_p_1.ljust(len(total_p_1) + calc_line_p_1 - 1, ' ') + "+"
calc_line_p_2 = len(cadre_result) - len(total_p_2)
total_p_2 = total_p_2.ljust(len(total_p_2) + calc_line_p_2 - 1, ' ') + "+"
print(cadre_result + '\n' + result_line + "\n" + total_p_1 + "\n" + total_p_2 + "\n" + cadre_result + '\n\n')
