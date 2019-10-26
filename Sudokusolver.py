#!/usr/bin/env python

board= 9*[9*[0]]

def check_row(row_pos, col_pos, num):
    legal_row = True
    if num in board[row_pos]:
        legal_row = False

    return legal_row


def check_col(row_pos, col_pos, num):
    legal_col = True
    for i in range (0,9)
        if board[i][col_pos] == num:
            legal_col = False

    return legal_col


def check_box(row_pos, col_pos, num):
    legal_box = True

    if 0 <= row_pos <= 2 and 0 <= col_pos <=2

    return legal_box


        



def check_legal(row_pos,col_pos,num):

    for row_pos in range(0,9):
        for col_pos in range(0,9):

            num_list=()
            for num in range (1,10):
                if board[row_pos][col_pos] != 0 :
                    legal_row=check_row(row_pos, col_pos, num)
                    legal_col=check_col(row_pos, col_pos,num)
                    legal_box=check_box(row_pos, col_pos, num)

                    if legal_row ==False and legal_col==False and legal_box==False:
                        num_list +=[num]

                    if len(num_list) ==1:
                        board[row_pos][col_pos] = num


print(board)
