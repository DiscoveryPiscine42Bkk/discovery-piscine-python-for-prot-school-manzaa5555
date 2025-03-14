class ChessBoard:
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.turn = "White"
        self.white_score = 0
        self.black_score = 0
        self.piece_values = {"p": 1, "n": 2, "b": 2, "r": 3, "q": 8, "k": 70,
                             "P": 1, "N": 2, "B": 2, "R": 3, "Q": 8, "K": 70}

    def display_board(self):
        black_color = "\033[30m"
        reset_color = "\033[39m"
        print(f"Current turn: {self.turn}")
        print(f"Scoreo) - White: {self.white_score} | Black: {self.black_score}")
        print(f"Max 100 (Pp=1 / Nn=2 / Bb=2 / Rr=3 / Qq=8 / Kk=70)=100")
        print("    a   b   c   d   e   f   g   h")
        for row in range(8):
            print(f"{8 - row}|", end=" ")
            for col in range(8):
                piece = self.board[row][col]
                if piece.islower():
                    print(f" {black_color}{piece}{reset_color} ", end="|")
                else:
                    print(f" {piece} ", end="|")
            print("\n  --------------------------------")
    
    def is_valid_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        
        if piece == "P":  # White Pawn
            if start_col == end_col and ((end_row == start_row - 1) or (start_row == 6 and end_row == 4)):
                return True
            if abs(end_col - start_col) == 1 and end_row == start_row - 1 and self.board[end_row][end_col].islower():
                return True
        elif piece == "p":  # Black Pawn
            if start_col == end_col and ((end_row == start_row + 1) or (start_row == 1 and end_row == 3)):
                return True
            if abs(end_col - start_col) == 1 and end_row == start_row + 1 and self.board[end_row][end_col].isupper():
                return True
        elif piece.lower() == "r":  # Rook
            if start_row == end_row or start_col == end_col:
                return True
        elif piece.lower() == "n":  # Knight
            if (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]:
                return True
        elif piece.lower() == "b":  # Bishop
            if abs(start_row - end_row) == abs(start_col - end_col):
                return True
        elif piece.lower() == "q":  # Queen
            if abs(start_row - end_row) == abs(start_col - end_col) or start_row == end_row or start_col == end_col:
                return True
        elif piece.lower() == "k":  # King
            if max(abs(start_row - end_row), abs(start_col - end_col)) == 1:
                return True
        return False
    
    def move_piece(self, start_pos, end_pos):
        if not self.is_valid_move(start_pos, end_pos):
            print("Invalid move! Try again.")
            return
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]
        captured_piece = self.board[end_row][end_col]
        
        if captured_piece != " ":
            if self.turn == "White":
                self.white_score += self.piece_values.get(captured_piece, 0)
            else:
                self.black_score += self.piece_values.get(captured_piece, 0)
        
        self.board[start_row][start_col] = " "
        self.board[end_row][end_col] = piece
        
        if captured_piece.lower() == "k":
            print(f"{self.turn} wins by capturing the King!")
            self.display_board()
            exit()
    
    def switch_turn(self):
        self.turn = "Black" if self.turn == "White" else "White"
    

def main():
    chess = ChessBoard()
    chess.display_board()
    
    while True:
        start_pos = input(f"{chess.turn}'s turn. Enter start position (e.g., 'a2') or 'exit' to quit: ")
        if start_pos.lower() == 'exit':
            print("Game Over.")
            break
        
        end_pos = input("Enter the end position (e.g., 'a3'): ")
        
        try:
            start_row = 8 - int(start_pos[1])
            start_col = ord(start_pos[0]) - ord('a')
            end_row = 8 - int(end_pos[1])
            end_col = ord(end_pos[0]) - ord('a')
        except (IndexError, ValueError):
            print("Invalid input, please enter a valid position like 'a2'.")
            continue
        
        chess.move_piece((start_row, start_col), (end_row, end_col))
        chess.switch_turn()
        chess.display_board()


if __name__ == "__main__":
    main()
