import cv2
import numpy as np
from chess_functions import *

board_img = cv2.imread('static/board_full.png')
threshold = 0.9

def find_pieces(board_img, templates=templates,method=cv2.TM_CCORR_NORMED , threshold = threshold, board=None):
    if board==None:
        board=init_board_dict()
    for piece in templates:
        match_template_result = cv2.matchTemplate(board_img, templates[piece][0], method, mask = templates[piece][1])
        ys,xs = np.where(match_template_result>=threshold)
        for i in range(len(xs)):
            if board[(xs[i]//square_pixel_size,ys[i]//square_pixel_size)] == 0:
                board[(xs[i]//square_pixel_size,ys[i]//square_pixel_size)] = f"{piece}"
    return board

board = find_pieces(board_img)

print(board)