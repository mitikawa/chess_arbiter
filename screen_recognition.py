import numpy as np
import cv2
from mss import mss
from PIL import Image
from chess_functions import *

bounding_box = {'top': 265, 'left': 820, 'width': 584, 'height': 584}

first = True
while True:
    if first:
        board_0 = recognize_pieces(cv2.imread('static/board_full.png'))
        first = False
    
    sct = mss()
    sct_img = sct.grab(bounding_box)
    sct_board = np.array(sct_img)

    sct_board = sct_board[:,:,:3]
    board_1 = recognize_pieces(sct_board)

    check_return = check_move(find_move(board_0,board_1))
    if check_return == 'not_recognized':
        print('Waiting...')
        cv2.waitKey(5000)
        continue

    #cv2.imshow('Current board', sct_board)
    board_0=board_1
    cv2.waitKey(5000)
