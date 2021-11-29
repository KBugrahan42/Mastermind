liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [' ',' ',' ',
                 ' ',' ',' ',
                 ' ',' ',' ',
                 ' '
                 ]
play_again = 0

def kazanma_durumu(board, choose):
    if(board[7] == board[8] == board[9] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[7] == board[4] == board[1] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[7] == board[5] == board[3] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[8] == board[5] == board[2] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[9] == board[6] == board[3] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[9] == board[5] == board[1] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[5] == board[4] == board[6] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[7] == board[4] == board[1] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[2] == board[3] == board[1] == choose):
        if(choose == player1_choose):
            print("Tebrikler Player 1 kazandı!")
            print_board(board)
            quit()
        elif(choose == player2_choose):
            print("Tebrikler Player 2 kazandı!")
            print_board(board)
            quit()
    if(board[1] != ' ' and board[2] != ' ' and board[3]!=' ' and board[4] != ' ' and board[5] != ' ' and board[6]!=' ' and board[7] != ' ' and board[8] != ' ' and board[9]!=' '):
        print("Oyun berabere bitti!")
        print_board(board)
        quit()
    else:
        return 0

def hamle(choice, number):
    board[number] = choice

def player_choose():

    while (True):
        global player1_choose
        global player2_choose

        player1_choose = input("Lutfen sembolunuzu seciniz!")

        if (player1_choose == 'X'):
            player2_choose = 'O'
            break

        elif (player1_choose == 'O'):
            player2_choose = 'X'
            break

        else:
            print("Lutfen gecerli olan bir sembol giriniz!")
            continue

def game():
    count = 0
    while(True):
        print_board(board)

        if(count % 2 == 0):
            print("Player 1 sıra sizde")
            numara = input("Hangi alana ekleme yapmak istediginizi giriniz!")

            if(numara.isdigit()):

                numara2 = int(numara)

            if(numara2 in range(0,10)):

                hamle(player1_choose,numara2)
                kazanma_durumu(board,player1_choose)
                count = count + 1
                continue

        elif(count % 2 != 0):
            print("Player 2 sıra sizde")
            numara = input("Hangi alana ekleme yapmak istediginizi giriniz!")

            if (numara.isdigit()):
                numara2 = int(numara)

            if (numara2 in range(0, 10)):
                hamle(player2_choose, numara2)
                kazanma_durumu(board, player2_choose)
                count = count + 1
                continue

def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

if __name__ == '__main__':
    player_choose()
    game()


