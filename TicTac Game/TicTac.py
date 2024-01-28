"""
Programmer: Estefany Hernández
"""
class TicTacToe:
    """
    A text-based Tic Tac Toe game.

    Attributes:
        board (list): The Tic Tac Toe board.
        current_player (str): The current player ('X' or 'O').
        winner (str): The winner of the game ('X', 'O', or 'Tie').
    """

    BOARD_SIZE = 3
    EMPTY_CELL = ' '
    PLAYERS = ['X', 'O']

    def __init__(self):
        """Initialize the game with an empty board and starting player."""
        self.board = [self.EMPTY_CELL] * self.BOARD_SIZE**2
        self.current_player = self.PLAYERS[0]
        self.winner = None

    def print_board(self):
        """Print the current state of the Tic Tac Toe board."""
        for i in range(0, len(self.board), self.BOARD_SIZE):
            print(" | ".join(self.board[i:i+self.BOARD_SIZE]))
            if i < len(self.board) - self.BOARD_SIZE:
                print("-" * (self.BOARD_SIZE * 4 - 1))

    def make_move(self, position):
        """
        Make a move on the board.

        Args:
            position (int): The position (1-9) where the player wants to make a move.
        """
        self.board[position - 1] = self.current_player

    def is_valid_move(self, position):
        """
        Check if the move is valid.

        Args:
            position (int): The position (1-9) where the player wants to make a move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return 1 <= position <= self.BOARD_SIZE**2 and self.board[position - 1] == self.EMPTY_CELL

    def switch_player(self):
        """Switch the current player."""
        self.current_player = self.PLAYERS[(self.PLAYERS.index(self.current_player) + 1) % len(self.PLAYERS)]

    def check_winner(self):
        """Check if there's a winner or if the game is a tie."""
        winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
                             (0, 4, 8), (2, 4, 6)]

        for row in winning_positions:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != self.EMPTY_CELL:
                self.winner = self.board[row[0]]
                return

        if self.EMPTY_CELL not in self.board:
            self.winner = 'Tie'

    def play_game(self):
        """Play the Tic Tac Toe game until there's a winner or a tie."""
        while not self.winner:
            print("\nCurrent Board:")
            self.print_board()
            try:
                position = int(input(f"\nPlayer {self.current_player}, enter your move (1-9): "))
                if not self.is_valid_move(position):
                    print("Invalid move. Please choose an empty cell (1-9).")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number (1-9).")
                continue

            self.make_move(position)
            self.check_winner()
            self.switch_player()

        print("\nFinal Board:")
        self.print_board()
        if self.winner == 'Tie':
            print("It's a tie!")
        else:
            print(f"Player {self.winner} wins!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
