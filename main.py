# Données sur les monstres et les attaques
monsters = {
    'pythachu': {
        'name': 'Pythachu',
        'attacks': ['tonnerre', 'charge'],
    },
    'pythard': {
        'name': 'Pytard',
        'attacks': ['jet-de-flotte', 'charge'],
    },
    'ponytha': {
        'name': 'Ponytha',
        'attacks': ['brûlure', 'charge'],
    },
}

attacks = {
    'charge': {'damages': 20},
    'tonnerre': {'damages': 50},
    'jet-de-flotte': {'damages': 40},
    'brûlure': {'damages': 40},
}

# Fonction pour saisir le nom et les PV d'un joueur
def saisie_nom_et_pv(player_name):
    while True:
        nom = input(f'Entrez le nom du {player_name} joueur : ').capitalize()
        pv = input('Et son nombre de PV : ')
        if pv.isdigit() and int(pv) > 0:
            return nom, int(pv)
        else:
            print('Nombre de PV invalide (doit être un nombre positif)')

# Fonction pour effectuer une attaque
def effectuer_attaque(attacker, defender):
    print(attacker['name'] + ', quelle attaque voulez-vous utiliser ?')
    for i, attack_name in enumerate(attacker['monster']['attacks'], 1):
        print(f'{i}: {attack_name.capitalize()} ({attacks[attack_name]["damages"]} PV)')
    
    while True:
        choice = input('> ')
        if choice.isdigit() and 1 <= int(choice) <= len(attacker['monster']['attacks']):
            attack_name = attacker['monster']['attacks'][int(choice) - 1]
            damages = attacks[attack_name]['damages']
            defender['pv'] -= damages
            print(f'{attacker["name"]} attaque {defender["name"]} qui perd {damages} PV.')
            print(f'{defender["name"]} a maintenant {defender["pv"]} PV.')
            break
        else:
            print('Attaque invalide, veuillez ressaisir le numéro.')

# Initialisation des joueurs
players = []
for i in range(2):
    player_name, player_pv = saisie_nom_et_pv(f'{i + 1}er') 
    monster_name = input('Choisissez votre monstre parmi ' + ', '.join(monsters.keys()) + ' : ')
    if monster_name in monsters:
        player = {
            'name': player_name,
            'pv': player_pv,
            'monster': monsters[monster_name]
        }
        players.append(player)
    else:
        print('Monstre invalide. Réessayez.')

# Boucle de combat
while all(player['pv'] > 0 for player in players): # all() vérifie que tous les joueurs ont encore des PV (return bool)
    for i, player in enumerate(players):
        other_player = players[1 - i]  # L'autre joueur
        effectuer_attaque(player, other_player)

# Affichage du résultat
print('La partie est terminée')
print('+ Résultat du combat +')
for player in players:
    print(f'{player["name"]} a {player["pv"]} PV')
