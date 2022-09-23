import cv2
import numpy as np
from chess_functions import *

#Starting board
board_img = cv2.imread('static/board_full.png')

#White pawn moves
board_img_e4 = cv2.imread('static/board_e4.png')
board_img_e3 = cv2.imread('static/board_e3.png')
board_img_e5 = cv2.imread('static/board_e5.png')
board_img_illegal_white_pawn_move = cv2.imread('static/board_illegal_white_pawn_move.png')

#Black pawn moves
board_img_e4_d6 = cv2.imread('static/board_e4_d6.png')
board_img_e4_d5 = cv2.imread('static/board_e4_d5.png')
board_img_e4_d4 = cv2.imread('static/board_e4_d4.png')

#Create board dictionary by doing template matching
board_original = recognize_pieces(board_img)
board_e4 = recognize_pieces(board_img_e4)
board_e3 = recognize_pieces(board_img_e3)
board_e5 = recognize_pieces(board_img_e5)
board_illegal = recognize_pieces(board_img_illegal_white_pawn_move)
board_e4_d6 = recognize_pieces(board_img_e4_d6)
board_e4_d5 = recognize_pieces(board_img_e4_d5)
board_e4_d4 = recognize_pieces(board_img_e4_d4)

#Check move validity - white pawn
'''check_move(find_move(board_original, board_e4))
check_move(find_move(board_original, board_e3))
check_move(find_move(board_original, board_e5))
check_move(find_move(board_original, board_illegal))
check_move(find_move(board_original, board_original))
check_move(find_move(board_e3, board_e5))
check_move(find_move(board_e4, board_original))'''

#Check move validity - black pawn
check_move(find_move(board_e4, board_e4_d6))
check_move(find_move(board_e4, board_e4_d5))
check_move(find_move(board_e4, board_e4_d4))
check_move(find_move(board_e4_d5, board_e4_d6))
check_move(find_move(board_e4_d6, board_e4_d4))
