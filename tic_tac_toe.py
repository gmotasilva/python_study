
#Cria um novo jogo
def create_new_game():
    print('Um novo jogo se inicia!')
    board = [['1a','2a','3a'], ['1b','2b','3b'] , ['1c','2c','3c']]

    return board

# atualiza o movimento do brother
def update_board(board, movement, move_count):
    for i in board:
        for y in range(0, 3):
            if i[y] == movement:
                if move_count % 2 == 0:
                    i[y] = 'x'
                else:
                    i[y] = 'y'
    return board


def show_board(board):
    for i in board:
        print(i[0], i[1], i[2])

# Pega a posição digitada pelo jogador

def get_player_move(board,move_count):
    movement=input('Digite a posição desejada\n')
    while check_valid_position(movement,board) is False:
        movement = input('Posição ja ocupada ou inválida Favor digite novamente\n')
    update_board(board, movement, move_count)
    move_count+=1
    return move_count, board

# Checa se a posição é valida
def check_valid_position(movement,board):
        for i in board:
            for y in range(0,3):
                if i[y] == movement:
                    return True
        return False



#verifica a porra do vencedor do jogo
def check_game_winner(board,move_count):
    if move_count % 2 == 0:
        if   board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
            return True
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
            return True
        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
             return True
        elif board[0][0] == 'x' and board[1][0] == 'x 'and board[2][0] == 'x':
            return True
        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
            return True
        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
            return True
        elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            return True
        elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            return True
    else:
            if  board[0][0] == 'y' and board[0][1] == 'y' and board[0][2] == 'y':
                return True
            elif board[1][0] == 'y 'and board[1][1] == 'y' and board[1][2] == 'y':
                return True
            elif board[2][0] == 'y' and board[2][1] == 'y' and board[2][2] == 'y':
                return True
            elif board[0][0] == 'y' and board[1][0] == 'y' and board[2][0] == 'y':
                return True
            elif board[0][1] == 'y' and board[1][1] == 'y' and board[2][1] == 'y':
                return True
            elif board[0][2] == 'y' and board[1][2] == 'y' and board[2][2] == 'y':
                return True
            elif board[0][0] == 'y' and board[1][1] == 'y' and board[2][2] == 'y':
                return True
            elif board[0][2] == 'y'and board[1][1] == 'y' and board[2][0] == 'y':
                return True
    return False

# Cria um novo jogo
board = create_new_game()
move_count = 0
show_board(board)
while move_count <= 8:
    print(move_count)
    get_player_move(board,move_count)
    show_board(board)
    if check_game_winner(board, move_count) is True:
        if move_count % 2 == 0:
                 print('Jogador X venceu')
                 break
        elif move_count % 2 == 1:
                print('Jogador Y venceu')
                break

    if move_count == 8:
            print('Deu velha')
            break
    move_count+=1
