import cv2
import numpy as np
from chess_functions import *


#Test on three sequential boards from a game

'''board_img_0 = cv2.imread('static/board_test_0.png')
board_img_1 = cv2.imread('static/board_test_1.png')
board_img_2 = cv2.imread('static/board_test_2.png')
board_img_3 = cv2.imread('static/board_test_3.png')

board_0 = recognize_pieces(board_img_0)
board_1 = recognize_pieces(board_img_1)
board_2 = recognize_pieces(board_img_2)
board_3 = recognize_pieces(board_img_3)


check_move(find_move(board_0,board_1))
check_move(find_move(board_1,board_2))
check_move(find_move(board_2,board_3))'''


board_0 = recognize_pieces(cv2.imread('static/board_test_mid_move.png'))
board_1 = recognize_pieces(cv2.imread('static/board_mid_movement.png'))

check_move(find_move(board_0,board_1))

