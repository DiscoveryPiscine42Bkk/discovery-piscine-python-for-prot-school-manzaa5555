# กำหนดขนาดกระดาน
BOARD_SIZE = 8

# สร้างกระดานหมากรุก
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

# กำหนดตัวแปร
selected_piece = None
selected_piece_pos = None
turn = "black"  # เปลี่ยนเป็น "black" เพื่อให้สีดำเริ่มก่อน
possible_moves = []  # เพิ่มตัวแปรสำหรับเก็บเส้นทางการเดินที่เป็นไปได้

# ฟังก์ชันวาดกระดานหมากรุก
def draw_board():
    # แสดงหมายเลขคอลัมน์
    print(" "+" "+"  ", end="")
    for col in range(BOARD_SIZE):
        print(chr(ord("a") + col) + " "+ " "+ " ", end="")
    print() 

    for row in range(BOARD_SIZE):
        print(str(8 - row) + " ", end="")  # แสดงหมายเลขแถว
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            piece_display = f"| {piece} "
            
            # เพิ่มการแสดงสี
            if piece.islower():  # ตัวพิมพ์เล็ก สีดำ
                piece_display = f"| \033[30m{piece}\033[0m "
            elif piece.isupper():  # ตัวพิมพ์ใหญ่ สีขาว
                piece_display = f"| \033[97m{piece}\033[0m "
            
            if (row, col) in possible_moves:  # แสดงเส้นทางการเดินที่เป็นไปได้
                print(f"| + ", end="")
            else:
                print(piece_display, end="")
        print("| " + str(8 - row))  # แสดงหมายเลขแถวอีกครั้ง

    # แสดงเส้นขอบด้านล่าง
    print("  " + "-" * (BOARD_SIZE * 4 + 1))

    # แสดงหมายเลขคอลัมน์อีกครั้ง
    print(" "+" "+"  ", end="")
    for col in range(BOARD_SIZE):
        print(chr(ord("a") + col) + " "+ " "+ " ", end="")
    print()

# ฟังก์ชันตรวจสอบการเดินหมากและแสดงเส้นทางการเดิน
def get_possible_moves(piece, start_pos):
    start_row, start_col = start_pos
    moves = []

    if piece.lower() == "p":  # เบี้ย
        if turn == "white":
            if start_row - 1 >= 0 and board[start_row - 1][start_col] == " ":
                moves.append((start_row - 1, start_col))
            if start_row == 6 and board[4][start_col] == " " and board[5][start_col] == " ":
                moves.append((4, start_col))
            if start_row - 1 >= 0 and start_col - 1 >= 0 and board[start_row - 1][start_col - 1] != " " and board[start_row - 1][start_col - 1].islower():
                moves.append((start_row - 1, start_col - 1))
            if start_row - 1 >= 0 and start_col + 1 < BOARD_SIZE and board[start_row - 1][start_col + 1] != " " and board[start_row - 1][start_col + 1].islower():
                moves.append((start_row - 1, start_col + 1))
        else:
            if start_row + 1 < BOARD_SIZE and board[start_row + 1][start_col] == " ":
                moves.append((start_row + 1, start_col))
            if start_row == 1 and board[3][start_col] == " " and board[2][start_col] == " ":
                moves.append((3, start_col))
            if start_row + 1 < BOARD_SIZE and start_col - 1 >= 0 and board[start_row + 1][start_col - 1] != " " and board[start_row + 1][start_col - 1].isupper():
                moves.append((start_row + 1, start_col - 1))
            if start_row + 1 < BOARD_SIZE and start_col + 1 < BOARD_SIZE and board[start_row + 1][start_col + 1] != " " and board[start_row + 1][start_col + 1].isupper():
                moves.append((start_row + 1, start_col + 1))

    elif piece.lower() == "r":  # เรือ
        for i in range(1, BOARD_SIZE):
            # ขึ้น
            if start_row - i >= 0 and board[start_row - i][start_col] == " ":
                moves.append((start_row - i, start_col))
            elif start_row - i >= 0 and board[start_row - i][start_col].isupper() if piece.islower() else board[start_row - i][start_col].islower():
                moves.append((start_row - i, start_col))
                break
            else:
                break
            # ลง
            if start_row + i < BOARD_SIZE and board[start_row + i][start_col] == " ":
                moves.append((start_row + i, start_col))
            elif start_row + i < BOARD_SIZE and board[start_row + i][start_col].isupper() if piece.islower() else board[start_row + i][start_col].islower():
                moves.append((start_row + i, start_col))
                break
            else:
                break
            # ซ้าย
            if start_col - i >= 0 and board[start_row][start_col - i] == " ":
                moves.append((start_row, start_col - i))
            elif start_col - i >= 0 and board[start_row][start_col - i].isupper() if piece.islower() else board[start_row][start_col - i].islower():
                moves.append((start_row, start_col - i))
                break
            else:
                break
            # ขวา
            if start_col + i < BOARD_SIZE and board[start_row][start_col + i] == " ":
                moves.append((start_row, start_col + i))
            elif start_col + i < BOARD_SIZE and board[start_row][start_col + i].isupper() if piece.islower() else board[start_row][start_col + i].islower():
                moves.append((start_row, start_col + i))
                break
            else:
                break

    elif piece.lower() == "n":  # ม้า
        knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        for move in knight_moves:
            new_row = start_row + move[0]
            new_col = start_col + move[1]
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
                if board[new_row][new_col] == " " or (board[new_row][new_col].islower() if piece.isupper() else board[new_row][new_col].isupper()):
                    moves.append((new_row, new_col))

    elif piece.lower() == "b":  # โคน
        for i in range(1, BOARD_SIZE):
            # ทแยงมุมซ้ายบน
            if start_row - i >= 0 and start_col - i >= 0 and board[start_row - i][start_col - i] == " ":
                moves.append((start_row - i, start_col - i))
            elif start_row - i >= 0 and start_col - i >= 0 and board[start_row - i][start_col - i].isupper() if piece.islower() else board[start_row - i][start_col - i].islower():
                moves.append((start_row - i, start_col - i))
                break
            else:
                break
            # ทแยงมุมขวาบน
            if start_row - i >= 0 and start_col + i < BOARD_SIZE and board[start_row - i][start_col + i] == " ":
                moves.append((start_row - i, start_col + i))
            elif start_row - i >= 0 and start_col + i < BOARD_SIZE and board[start_row - i][start_col + i].isupper() if piece.islower() else board[start_row - i][start_col + i].islower():
                moves.append((start_row - i, start_col + i))
                break
            else:
                break
            # ทแยงมุมซ้ายล่าง
            if start_row + i < BOARD_SIZE and start_col - i >= 0 and board[start_row + i][start_col - i] == " ":
                moves.append((start_row + i, start_col - i))
            elif start_row + i < BOARD_SIZE and start_col - i >= 0 and board[start_row + i][start_col - i].isupper() if piece.islower() else board[start_row + i][start_col - i].islower():
                moves.append((start_row + i, start_col - i))
                break
            else:
                break
            # ทแยงมุมขวาล่าง
            if start_row + i < BOARD_SIZE and start_col + i < BOARD_SIZE and board[start_row + i][start_col + i] == " ":
                moves.append((start_row + i, start_col + i))
            elif start_row + i < BOARD_SIZE and start_col + i < BOARD_SIZE and board[start_row + i][start_col + i].isupper() if piece.islower() else board[start_row + i][start_col + i].islower():
                moves.append((start_row + i, start_col + i))
                break
            else:
                break

    elif piece.lower() == "q":  # ควีน
        moves.extend(get_possible_moves("r", start_pos))  # เรือ
        moves.extend(get_possible_moves("b", start_pos))  # โคน

    elif piece.lower() == "k":  # คิง
        king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for move in king_moves:
            new_row = start_row + move[0]
            new_col = start_col + move[1]
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
                if board[new_row][new_col] == " " or (board[new_row][new_col].islower() if piece.isupper() else board[new_row][new_col].isupper()):
                    moves.append((new_row, new_col))
    return moves

# ฟังก์ชันตรวจสอบสถานะของราชา
def check_king_status():
    white_king = black_king = False
    
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece == "K":
                white_king = True
            elif piece == "k":
                black_king = True

    if not white_king:
        return "Black wins! White's king is captured."
    elif not black_king:
        return "White wins! Black's king is captured."
    
    return None  # ไม่มีใครชนะ

# ฟังก์ชันตรวจสอบการเดินหมาก
def is_valid_move(piece, start_pos, end_pos):
    return end_pos in possible_moves  # ตรวจสอบว่าตำแหน่งที่จะเดินอยู่ในเส้นทางการเดินที่เป็นไปได้หรือไม่

# ฟังก์ชันถามผู้เล่นว่าจะเล่นรอบใหม่ไหม
def ask_to_play_again():
    while True:
        answer = input("Would you like to play another round? (yes/no): ").lower()
        if answer == "yes":
            print("Next round!")
            return True
        elif answer == "no":
            print("Stop the game.")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# เริ่มเกม
draw_board()

# วนรอบเกม
while True:
    # รับอินพุตจากผู้ใช้
    move = input(f"{turn} turn. Enter move (e.g. a2 or a2 a4): ")
    if move == "exit":
        break

    # แยกอินพุต
    try:
        moves = move.split()
        start_pos = moves[0]
        start_col, start_row = ord(start_pos[0]) - ord("a"), 8 - int(start_pos[1])
        if len(moves) == 2:
            end_pos = moves[1]
            end_col, end_row = ord(end_pos[0]) - ord("a"), 8 - int(end_pos[1])
        else:
            end_col, end_row = None, None
    except (ValueError, IndexError):
        print("Invalid move. Try again.")
        continue

    # ตรวจสอบว่ามีการเลือกหมากหรือไม่
    if selected_piece is None:
        # เลือกหมากและแสดงเส้นทางการเดิน
        selected_piece = board[start_row][start_col]
        if selected_piece != " ":
            selected_piece_pos = (start_row, start_col)
            possible_moves = get_possible_moves(selected_piece, selected_piece_pos)
            # วาดกระดานใหม่
            draw_board()
        else:
            print("No piece selected. Try again.")
            continue
    elif end_col is not None and end_row is not None:
        # เดินหมาก
        if is_valid_move(selected_piece, selected_piece_pos, (end_row, end_col)):
            # สลับตำแหน่งหมาก
            board[end_row][end_col] = selected_piece
            board[selected_piece_pos[0]][selected_piece_pos[1]] = " "
            
            # ตรวจสอบสถานะของราชา
            game_result = check_king_status()
            if game_result:
                print(game_result)
                # ถามผู้เล่นว่าจะเล่นต่อหรือไม่
                if not ask_to_play_again():
                    break  # จบเกม

            # สลับตาเดิน
            turn = "white" if turn == "black" else "black"
            # รีเซ็ตตัวแปร
            selected_piece = None
            selected_piece_pos = None
            possible_moves = []
            # วาดกระดานใหม่
            draw_board()
        else:
            print("Invalid move. Try again.")
            # รีเซ็ตตัวแปร
            selected_piece = None
            selected_piece_pos = None
            possible_moves = []
            continue
