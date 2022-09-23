import cv2
import numpy as np
from chess_functions import *

#Starting board
'''board_img = cv2.imread('static/board_full.png')
board_original = recognize_pieces(board_img)'''

#White pawn moves
'''board_img_e4 = cv2.imread('static/board_e4.png')
board_img_e3 = cv2.imread('static/board_e3.png')
board_img_e5 = cv2.imread('static/board_e5.png')
board_img_illegal_white_pawn_move = cv2.imread('static/board_illegal_white_pawn_move.png')

board_e4 = recognize_pieces(board_img_e4)
board_e3 = recognize_pieces(board_img_e3)
board_e5 = recognize_pieces(board_img_e5)
board_illegal = recognize_pieces(board_img_illegal_white_pawn_move)
'''
#Check move validity - white pawn
'''check_move(find_move(board_original, board_e4))
check_move(find_move(board_original, board_e3))
check_move(find_move(board_original, board_e5))
check_move(find_move(board_original, board_illegal))
check_move(find_move(board_original, board_original))
check_move(find_move(board_e3, board_e5))
check_move(find_move(board_e4, board_original))'''

#Black pawn moves
'''board_img_e4_d6 = cv2.imread('static/board_e4_d6.png')
board_img_e4_d5 = cv2.imread('static/board_e4_d5.png')
board_img_e4_d4 = cv2.imread('static/board_e4_d4.png')

board_e4_d6 = recognize_pieces(board_img_e4_d6)
board_e4_d5 = recognize_pieces(board_img_e4_d5)
board_e4_d4 = recognize_pieces(board_img_e4_d4)'''

#Check move validity - black pawn
'''check_move(find_move(board_e4, board_e4_d6))
check_move(find_move(board_e4, board_e4_d5))
check_move(find_move(board_e4, board_e4_d4))
check_move(find_move(board_e4_d5, board_e4_d6))
check_move(find_move(board_e4_d6, board_e4_d4))'''


#Rook moves
'''board_img_rook_0 = cv2.imread('static/board_with_two_towers.png')
board_img_rook_1 = cv2.imread('static/board_rf1_rb4.png')
board_img_rook_2 = cv2.imread('static/board_illegal_rook_move.png')

board_rook_0 = recognize_pieces(board_img_rook_0)
board_rook_1 = recognize_pieces(board_img_rook_1)
board_rook_2 = recognize_pieces(board_img_rook_2)'''

#check move validity - rooks

'''check_move(find_move(board_rook_0,board_rook_1))
check_move(find_move(board_rook_0,board_rook_2))'''


#Bishop moves
'''board_img_bishop_0 = cv2.imread('static/board_bishop_base.png')
board_img_bishop_1 = cv2.imread('static/board_bishop_valid.png')
board_img_bishop_2 = cv2.imread('static/board_bishop_illegal.png')

board_bishop_0 = recognize_pieces(board_img_bishop_0)
board_bishop_1 = recognize_pieces(board_img_bishop_1)
board_bishop_2 = recognize_pieces(board_img_bishop_2)'''

#Check move vailidity - bishops

'''check_move(find_move(board_bishop_0,board_bishop_1))
check_move(find_move(board_bishop_0,board_bishop_2))'''


# King moves
'''board_img_king_0 = cv2.imread('static/board_with_king.png')
board_img_king_1 = cv2.imread('static/board_valid_move.png')
board_img_king_2 = cv2.imread('static/board_illegal_move.png')

board_king_0 = recognize_pieces(board_img_king_0)
board_king_1 = recognize_pieces(board_img_king_1)
board_king_2 = recognize_pieces(board_img_king_2)'''

#Check move vailidity - kings
'''
check_move(find_move(board_king_0,board_king_1))
check_move(find_move(board_king_0,board_king_2))'''


# knight moves
'''board_img_knight_0 = cv2.imread('static/board_knight_base.png')
board_img_knight_1 = cv2.imread('static/board_knight_valid.png')
board_img_knight_2 = cv2.imread('static/board_knight_illegal.png')

board_knight_0 = recognize_pieces(board_img_knight_0)
board_knight_1 = recognize_pieces(board_img_knight_1)
board_knight_2 = recognize_pieces(board_img_knight_2)'''

#Check move vailidity - knights

'''check_move(find_move(board_knight_0,board_knight_1))
check_move(find_move(board_knight_0,board_knight_2))'''

# Queen moves
board_img_queen_0 = cv2.imread('static/board_queen_base.png')
board_img_queen_1 = cv2.imread('static/board_queen_illegal.png')
board_img_queen_2 = cv2.imread('static/board_queen_adjacent.png')
board_img_queen_3 = cv2.imread('static/board_queen_rook_like.png')
board_img_queen_4 = cv2.imread('static/board_queen_bishop_like.png')

board_queen_0 = recognize_pieces(board_img_queen_0)
board_queen_1 = recognize_pieces(board_img_queen_1)
board_queen_2 = recognize_pieces(board_img_queen_2)
board_queen_3 = recognize_pieces(board_img_queen_3)
board_queen_4 = recognize_pieces(board_img_queen_4)



#Check move vailidity - queens

check_move(find_move(board_queen_0,board_queen_1))
check_move(find_move(board_queen_0,board_queen_2))
check_move(find_move(board_queen_0,board_queen_3))
check_move(find_move(board_queen_0,board_queen_4))