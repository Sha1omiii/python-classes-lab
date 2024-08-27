# User Stories
# Your goal is to implement the following user stores:

# As a user (AAU), I want to see a welcome message at the start of a game.
# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
# AAU, at the beginning of each turn, told whose turn it is: It’s player X’s turn!
# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
# AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.

class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None, 
        }
        
    def play_game(self):
        print('Welcome to a python tic-tac-toe game.')

    def render_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    
    def render_msg(self):
        if self.tie:
            print('Tie game')
        elif self.winner:
            print(f'{self.winner} won the game')
        else:
            print(f'Player {self.turn}\'s turn!')
        
    
    def handle_user_input(self):
        while True:

            user_move = input('Enter your move (valid: example A1 or C3): ').lower()
            if user_move in self.board:
                self.board[user_move] = self.turn
                break
            else:
                print('Invalid input. Please try again.')
                continue
            
    # def check_winner(self):
    # check the board for winning conditions (8)
    # a loop to check winning conditions
    # if there is a winner, update the current player turn to reflect the winner

    # def check_tie(self):
    # if all spaces in the board are filled with no positions marked as None and there is no winner, then tie = true

    def switch_turn(self):
    # at the end of every turn, alternate between x and o
    # a lookup table using dictionary 
        lookup_table = {'X': 'O', 'O': 'X'}
        self.turn = lookup_table[self.turn]

    # def play_game(self):
    # as long as there is no winner or tie, game continues
    #     print('Wanna play again.')
    #     while self.winner == None:
    #         self.play_game()
    #         self.render_board()
    #         self.render_msg()
    #         self.handle_user_input()
    #         self.render_board()
        



game1 = Game()
game1.play_game()
game1.render_board()
game1.render_msg()
game1.handle_user_input()
game1.render_board()