import pygame

pygame.init()

x=1
y=1

def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def place(position):
    r = "white_rook.png"
    n = "white_knight.png"
    b = "white_bishop.png"
    q = "white_queen.png"
    k = "white_king.png"
    p = "white_pawn.png"

    R = "black_rook.png"
    N = "black_knight.png"
    B = "black_bishop.png"
    Q = "black_queen.png"
    K = "black_king.png"
    P = "black_pawn.png"
    row = 0
    column = 0
    for i in range(len(position)):
        if position[i] == "/":
            row += 1
            column = 0
            continue
        elif isInt(position[i]) == True:
            if int(position[i])==8:
                row += 1
                continue
            else:
                column += (int(position[i])-1)
        elif position[i] == "r": # Rook
            win.blit(pygame.transform.scale(pygame.image.load(r), (60,75)),((column*100)+19,(row*100)+15))
        elif position[i] == "n": # Knight
            win.blit(pygame.transform.scale(pygame.image.load(n), (69,78)),((column*100)+10,(row*100)+10))
        elif position[i] == "b": # Bishop
            win.blit(pygame.transform.scale(pygame.image.load(b), (65,80)),((column*100)+14,(row*100)+8))
        elif position[i] == "q": # Queen
            win.blit(pygame.transform.scale(pygame.image.load(q), (79,80)),((column*100)+10,(row*100)+8))
        elif position[i] == "k": # King
            win.blit(pygame.transform.scale(pygame.image.load(k), (75,80)),((column*100)+12,(row*100)+8))
        elif position[i] == "p": # Pawn
            win.blit(pygame.transform.scale(pygame.image.load(p), (50,65)),((column*100)+26,(row*100)+18))
        elif position[i] == "R": # Rook
            win.blit(pygame.transform.scale(pygame.image.load(R), (60,75)),((column*100)+19,(row*100)+15))
        elif position[i] == "N": # Knight
            win.blit(pygame.transform.scale(pygame.image.load(N), (69,78)),((column*100)+10,(row*100)+10))
        elif position[i] == "B": # Bishop
            win.blit(pygame.transform.scale(pygame.image.load(B), (65,80)),((column*100)+14,(row*100)+8))
        elif position[i] == "Q": # Queen
            win.blit(pygame.transform.scale(pygame.image.load(Q), (79,80)),((column*100)+10,(row*100)+8))
        elif position[i] == "K": # King
            win.blit(pygame.transform.scale(pygame.image.load(K), (75,80)),((column*100)+12,(row*100)+8))
        elif position[i] == "P": # Pawn
            win.blit(pygame.transform.scale(pygame.image.load(P), (50,65)),((column*100)+26,(row*100)+18))
        column += 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_board():
    board = pygame.transform.scale(pygame.image.load("chess_board.png"), (800,800))
    win.blit(board, (0,0))

draw_board()
place("RNBQKBNR/PPPPPPPP///3pq2Q//ppp1pppp/rnbqkbnr")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicked ")
            print(pygame.mouse.get_pos())
            print("\n")
    pygame.display.update()

pygame.quit()

# def draw_pieces():
#     global x,y
#     if x>=0 and y>=0:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_w:
#                     print("W\n")
#                     y-=1
#                 if event.key == pygame.K_s:
#                     print("S\n")
#                     y+=1
#                 if event.key == pygame.K_d:
#                     print("D\n")
#                     x+=1
#                 if event.key == pygame.K_a:
#                     print("A\n")
#                     x-=1
#     white_knight = Pieces("rook", "white")
#     white_knight.place(x,y)

# def board_position():
#     initial_position = ("rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook")
#     position_white = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]]
#     position_black = [[0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8]]

#     white_rook = Pieces("rook", "white")
#     white_knight = Pieces("knight", "white")
#     white_bishop = Pieces("bishop", "white")
#     white_queen = Pieces("queen", "white")
#     white_king = Pieces("king", "white")

#     black_rook = Pieces("rook", "black")
#     black_knight = Pieces("knight", "black")
#     black_bishop = Pieces("bishop", "black")
#     black_queen = Pieces("queen", "black")
#     black_king = Pieces("king", "black")

# white_pieces = ["white_rook.png", "white_knight.png", "white_bishop.png", "white_queen.png", "white_king.png", "white_pawn.png"]
# black_pieces = ["black_rook.png", "black_knight.png", "black_bishop.png", "black_queen.png", "black_king.png", "black_pawn.png"]
# if self.name.lower() == "rook" and self.color == "white":
#     win.blit(pygame.transform.scale(pygame.image.load(white_pieces[0]), (65,80)),((coordinate_x*100)+2,(coordinate_y*100)+6))
# elif self.name.lower() == "knight" and self.color == "white":
#     win.blit(pygame.transform.scale(pygame.image.load(white_pieces[1]), (65,80)),((coordinate_x*100)+16,(coordinate_y*100)+6))
# elif self.name.lower() == "bishop" and self.color == "white":
#     win.blit(pygame.transform.scale(pygame.image.load(white_pieces[2]), (70,70)),((coordinate_x*100)+13,(coordinate_y*100)+6))
# elif self.name.lower() == "queen" and self.color == "white":
#     win.blit(pygame.transform.scale(pygame.image.load(white_pieces[3]), (80,80)),((coordinate_x*100)+2,(coordinate_y*100)+6))
# elif self.name.lower() == "king" and self.color == "white":
#     win.blit(pygame.transform.scale(pygame.image.load(white_pieces[4]), (80,80)),((coordinate_x*100)+8,(coordinate_y*100)+6))

# elif self.name.lower() == "rook" and self.color == "black":
#     win.blit(pygame.transform.scale(pygame.image.load(black_pieces[0]), (65,80)),((coordinate_x*100)+16,(coordinate_y*100)+6))
# elif self.name.lower() == "knight" and self.color == "black":
#     win.blit(pygame.transform.scale(pygame.image.load(black_pieces[1]), (65,80)),((coordinate_x*100)+16,(coordinate_y*100)+6))
# elif self.name.lower() == "bishop" and self.color == "black":
#     win.blit(pygame.transform.scale(pygame.image.load(black_pieces[2]), (70,70)),((coordinate_x*100)+13,(coordinate_y*100)+6))
# elif self.name.lower() == "queen" and self.color == "black":
#     win.blit(pygame.transform.scale(pygame.image.load(black_pieces[3]), (80,80)),((coordinate_x*100)+2,(coordinate_y*100)+6))
# elif self.name.lower() == "king" and self.color == "black":
#     win.blit(pygame.transform.scale(pygame.image.load(black_pieces[4]), (80,80)),((coordinate_x)*100+8,(coordinate_y*100)+6))

#     white_rook.place(position_white[0][0], position_white[0][1])
#     white_knight.place(position_white[1][0], position_white[1][1])
#     white_bishop.place(position_white[2][0], position_white[2][1])
#     white_queen.place(position_white[3][0], position_white[3][1])
#     white_king.place(position_white[4][0], position_white[4][1])
#     white_bishop.place(position_white[5][0], position_white[5][1])
#     white_knight.place(position_white[6][0], position_white[6][1])
#     white_rook.place(position_white[7][0], position_white[7][1])

#     black_rook.place(position_black[0][0], position_black[0][1])
#     black_knight.place(position_black[1][0], position_black[1][1])
#     black_bishop.place(position_black[2][0], position_black[2][1])
#     black_queen.place(position_black[3][0], position_black[3][1])
#     black_king.place(position_black[4][0], position_black[4][1])
#     black_bishop.place(position_black[5][0], position_black[5][1])
#     black_knight.place(position_black[6][0], position_black[6][1])
#     black_rook.place(position_black[7][0], position_black[7][1])

# def board_position():
#     position = 
    # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
