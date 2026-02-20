# Object-Oriented Tic Tac Toe Game (X O)

class TicTacToe:
    def __init__(self):
        # Initialize an empty board with 9 spaces
        self.board = [" " for _ in range(9)]
        # Start with player X
        self.current_player = "X"

    def print_board(self):
        """Prints the current state of the board"""
        print("\n")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("--+---+--")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("--+---+--")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])
        print("\n")

    def check_winner(self):
        """Checks if the current player has won"""
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]
        for condition in win_conditions:
            if (self.board[condition[0]] == self.current_player and
                self.board[condition[1]] == self.current_player and
                self.board[condition[2]] == self.current_player):
                return True
        return False

    def check_draw(self):
        """Checks if the game is a draw"""
        return " " not in self.board

    def switch_player(self):
        """Switches the current player"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self, position):
        """Places a mark on the board if valid"""
        if position < 0 or position > 8:
            print("Invalid position! Choose 1-9.")
            return False
        if self.board[position] != " ":
            print("Position already taken!")
            return False
        self.board[position] = self.current_player
        return True

    def play(self):
        """Runs the game loop"""
        while True:
            self.print_board()
            try:
                pos = int(input(f"Player {self.current_player}, choose a position (1-9): ")) - 1
            except ValueError:
                print("Please enter a valid number!")
                continue

            if not self.make_move(pos):
                continue

            if self.check_winner():
                self.print_board()
                print(f"🎉 Player {self.current_player} wins!")
                break

            if self.check_draw():
                self.print_board()
                print("🤝 It's a draw!")
                break

            self.switch_player()


# Start the game
game = TicTacToe()
game.play()
