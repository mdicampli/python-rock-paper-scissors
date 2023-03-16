import random


class Game:
    def __init__(self):
        self.user_score = 0
        self.pc_score = 0
        self.moves = {'sasso': 0, 'carta': 1, 'forbice': 2}
        self.games_played = 0
        self.user_wins = 0
        self.pc_wins = 0

    def play(self):
        while True:
            print(f'User {self.user_score} - PC {self.pc_score}')
            user_move = input(
                'Scegli una mossa: \n 0 - Sasso\n 1 - Carta\n 2 - Forbice\n 3 - Resetta i punteggi\n 4 - Esci\n')
            if user_move == '3':
                self.reset_scores()
                self.games_played += 1
                print('Punteggi resettati')
            elif user_move == '4':
                self.games_played += 1
                self.print_result()
                break
            else:
                if user_move not in ['0', '1', '2']:
                    print('Input non valido')
                    continue
                user_move = int(user_move)
                pc_move = random.randint(0, 2)
                if user_move == pc_move:
                    print('Pareggio')
                elif (user_move == self.moves['sasso'] and pc_move == self.moves['forbice'] or
                      user_move == self.moves['carta'] and pc_move == self.moves['sasso'] or
                      user_move == self.moves['forbice'] and pc_move == self.moves['carta']):
                    print('Hai vinto!')
                    self.user_score += 1
                    self.user_wins += 1
                else:
                    print('Hai perso!')
                    self.pc_score += 1
                    self.pc_wins += 1

    def reset_scores(self):
        self.user_score = 0
        self.pc_score = 0

    def print_result(self):
        print(f'Partite giocate: {self.games_played}')
        print(f'Utente: {self.user_wins} vittorie, {self.pc_wins} sconfitte')
        print(f'PC: {self.pc_wins} vittorie, {self.user_wins} sconfitte')


if __name__ == "__main__":
    Game().play()
