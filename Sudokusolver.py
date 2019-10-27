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


def make_box(row_pos, col_pos):
    box  = []
    box_dict={1:[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)], 2:[(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)], }


def check_box(row_pos, col_pos, num):
    legal_box = True
    coordinate=row_pos,col_pos
    for i in range(9)
        if coordinate in box_dict{i}:
            for k in box_dict{i}:
                row_pos,col_pos=k
                if board[row_pos][col_pos] == num:
                    legal_box = False


                    return legal_box



#I pos. (0,0) vil me sjekke board[0][0] til board[0][2], board[1][0] og board[2][0]





def check_legal(row_pos,col_pos,num):

    for row_pos in range(0,9):
        for col_pos in range(0,9):

            num_list=[]
            if board[row_pos][col_pos] == 0 :
                for num in range (1,10):
                    legal_row=check_row(row_pos, col_pos, num)
                    legal_col=check_col(row_pos, col_pos,num)
                    legal_box=check_box(row_pos, col_pos, num)

                    if legal_row ==True and legal_col==True and legal_box==True:
                        num_list +=[num]

            if len(num_list) == 1:
                board[row_pos][col_pos] = num_list[0]


print(board)
