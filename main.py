import cv2
import numpy as np
from chess_functions import *

board_img = cv2.imread('static/board_full.png')
board_img_e4 = cv2.imread('static/board_e4.png')
board_img_e3 = cv2.imread('static/board_e3.png')
board_img_e5 = cv2.imread('static/board_e5.png')
board_img_illegal_white_pawn_move = cv2.imread('static/board_illegal_white_pawn_move.png')

board_original = recognize_pieces(board_img)
board_e4 = recognize_pieces(board_img_e4)
board_e3 = recognize_pieces(board_img_e3)
board_e5 = recognize_pieces(board_img_e5)
board_illegal = recognize_pieces(board_img_illegal_white_pawn_move)


check_move(find_move(board_original, board_e4))
check_move(find_move(board_original, board_e3))
check_move(find_move(board_original, board_e5))
check_move(find_move(board_original, board_illegal))
check_move(find_move(board_original, board_original))
check_move(find_move(board_e3, board_e5))
check_move(find_move(board_e4, board_original))


