---
id: da354a-ht23
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning - Extra

<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/tpdFCDCVxbA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Nästlade listor som tabeller

![picture](../images/movies.jpg)

```python
filmer = [
    ["Titel", "År", "Regissör"],
    ["Star Wars", "1977", "George Lucas"],
    ["Inception", "2010", "Christopher Nolan"],
    ["Fight club", "1999", "David Fincher"]
]

filmer.append([
    "Titanic",
    "1997",
    "James Cameron"
])

filmer.remove(["Inception", "2010", "Christopher Nolan"])

removed_movie = filmer.pop()
print(f"Vi tog bort filmen {removed_movie[0]}\n")

for film in filmer:
    for item in film:
        print(f"{item:^12}", end="")

    print()
```

### 3-i-rad

![picture](../images/3-i-rad-1.jpg)
![picture](../images/3-i-rad-2.jpg)

```python
import random

def game():
    print("*"*11)
    print("Tre-i-rad")
    print("*"*11)

    game_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    turn = random.randint(0, 1)

    winner = False

    print_game_board(game_board)

    while not winner:
        if turn % 2 == 0:
            # Vår tur
            while True:
                row = int(input("Rad: "))
                col = int(input("Kolumn: "))

                if make_guess(game_board, row, col, "X"):
                    break

                print("Du angav inte ett giltigt val, försök igen!")
            
        else:
            # Datorns tur
            print("Datorns tur...")
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)

                if make_guess(game_board, row, col, "O"):
                    break

        print_game_board(game_board)

        winner = get_winner(game_board)
        
        turn += 1

    if winner == "X":
        print("Grattis du vann!")
    elif winner == "O":
        print("Datorn vann!")
    else:
        print("Lika!")

def get_winner(board):
    for player in ["X", "O"]:
        # 1. Kontrollera horisontellt
        if get_row_win(board, player):
            return player
        # 2. Kontrollera vertikalt
        elif get_col_win(board, player):
            return player
        # 3. Kontrollera diagonalt (start uppe till vänster)
        elif get_dia_win_1(board, player):
            return player
        # 4. Kontrollera diagonalt (start uppe höger)
        elif get_dia_win_2(board, player):
            return player
        # 5. Om det är lika
        else:
            free_slots = 0
            for row in board:
                free_slots = row.count(" ")

            if free_slots == 0:
                return "-"

    return False

def get_row_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    return False

def get_col_win(board, player):
    for i in range(3):
        win = True
        for j in range(3):
            if board[j][i] != player:
                win = False
        if win == True:
            return True

    return False

def get_dia_win_1(board, player):
    win = True
    for x in range(3):
        if board[x][x] != player:
            win = False

    return win

def get_dia_win_2(board, player):
    win = True
    for x in range(3):
        if board[x][3-(x+1)] != player:
            win = False
    
    return win

def make_guess(board, row, col, player):
    if row < 0 or row > 2:
        return False
    elif col < 0 or col > 2:
        return False
    elif board[row][col] != " ":
        return False
    else:
        board[row][col] = player
        return True

def print_game_board(board):
    print("-"*11)
    for row in board:
        print(" " + " | ".join(row))
        print("-"*11)

game()
```


### x-i-rad (bättre (mer generell) lösning)

```python
import random

def game():
    nr = int(input("Hur många i rad vill du spela? "))
    
    print("*"*11)
    print("{} i rad".format(nr))
    print("*"*11)

    game_board = []
    for i in range(nr):
        game_board.append([" "]*nr)

    print_game_board(game_board)

    turn = random.randint(0, 1)

    winner = False

    while not winner:
        if turn % 2 == 0:
            # Vår tur
            while True:
                row = int(input("Rad: "))
                col = int(input("Kolumn: "))
                
                if make_guess(game_board, row, col, "X"):
                    break

                print("Du angav inte ett giltigt val, försök igen!")
        else:
            # Datorn tur
            print("Datorns tur...")
            while True:
                row = random.randint(0, len(game_board)-1)
                col = random.randint(0, len(game_board)-1)

                if make_guess(game_board, row, col, "O"):
                    break

        print_game_board(game_board)

        winner = get_winner(game_board, ["X", "O"])

        turn += 1

    if winner == "X":
        print("Grattis! Du slog datorn!")
    elif winner == "-":
        print("Lika!")
    else:
        print("Ajdå, datorn vann...")

def get_winner(board, players):
    for player in players:
        # 1. Kontrollera horisontellt
        if get_row_win(board, player):
            return player
        # 2. Kontrollera vertikalt
        elif get_col_win(board, player):
            return player
        # 3. Kontrollera diagonalt (start uppe vänster)
        elif get_dia_win_1(board, player):
            return player
        # 4. Kontrollera diagonalt (start nere vänster)
        elif get_dia_win_2(board, player):
            return player
        # 5. Kontrollera om det är LIKA!
        else:
            free_slots = 0
            for row in board:
                free_slots += row.count(" ")

            if free_slots == 0:
                return "-"

    return False

def get_row_win(board, player):
    for row in board:
        if row.count(player) == len(board):
            return True

    return False

def get_col_win(board, player):
    win = True
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
        if win:
            return True

    return False

def get_dia_win_1(board, player):
    win = True
    for x in range(len(board)):
        if board[x][x] != player:
            win = False

    return win

def get_dia_win_2(board, player):
    win = True
    for x in range(len(board)):
        if board[x][len(board)-(x+1)] != player:
            win = False
    
    return win
    
def make_guess(board, row, col, player):
    if row < 0 or row > len(board)-1:
        return False
    elif col < 0 or col > len(board)-1:
        return False
    elif board[row][col] != " ":
        return False
    else:
        board[row][col] = player
        return True

def print_game_board(board):
    game_length = (3*len(board)) + len(board)-1
    print("-"*game_length)
    for row in board:
        print(" " + " | ".join(row))
        print("-"*game_length)
    
game()
```