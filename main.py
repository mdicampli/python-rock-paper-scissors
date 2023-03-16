import random

# Inizializza i punteggi
user_score = 0
pc_score = 0

# Dizionario per associare le mosse a dei numeri
moves = {'sasso': 0, 'carta': 1, 'forbice': 2}

while True:
    # Mostra i punteggi attuali
    print(f'User {user_score} - PC {pc_score}')

    # Chiede all'utente di scegliere una mossa
    user_move = input('Scegli una mossa: \n 0 - Sasso\n 1 - Carta\n 2 - Forbice\n 3 - Resetta i punteggi\n 4 - Esci\n')

    # Gestisce le diverse scelte dell'utente
    if user_move == '3':
        # Resetta i punteggi
        user_score = 0
        pc_score = 0
        print('Punteggi resettati')
    elif user_move == '4':
        # Termina il gioco
        print('Fine gioco')
        break
    else:
        # Verifica che l'input dell'utente sia valido
        if user_move not in ['0', '1', '2']:
            print('Input non valido')
            continue

        # Converte la mossa dell'utente in un intero
        user_move = int(user_move)

        # Genera la mossa del computer in modo casuale
        pc_move = random.randint(0, 2)

        # Confronta le mosse e aggiorna i punteggi
        if user_move == pc_move:
            print('Pareggio')
        elif (user_move == moves['sasso'] and pc_move == moves['forbice'] or
              user_move == moves['carta'] and pc_move == moves['sasso'] or
              user_move == moves['forbice'] and pc_move == moves['carta']):
            print('Hai vinto!')
            user_score += 1
        else:
            print('Hai perso!')
            pc_score += 1
