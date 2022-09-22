import cv2
import numpy as np

board_img = cv2.imread('static/board_with_two_towers.png')
tower_template = cv2.imread('static/tower_grey.png')
square_pixel_size = int(board_img.shape[0]/8)
threshold=0.8

def get_square_name(coordinates):
    columns = 'abcdefgh'
    square = columns[coordinates[0]]+str(8-coordinates[1])
    return square

def init_board_dict():
    board_dict = {}
    for i in range(0,7):
        for j in range(0,7):
            board_dict[(i,j)]=0
    return board_dict


def find_tower(board_img, template=tower_template,method=cv2.TM_CCOEFF_NORMED, threshold = threshold, board=init_board_dict()):
    match_template_result = cv2.matchTemplate(board_img, template,method)
    ys,xs = np.where(match_template_result>=threshold)
    for i in range(len(xs)):
        board[(xs[i]//square_pixel_size,ys[i]//square_pixel_size)] = 'tower'
    return board

def get_towers_positions(board):
    return [get_square_name(key) for key,value in board_with_pieces.items() if value=='tower']

board_with_pieces = find_tower(board_img)

for tower in get_towers_positions(board_with_pieces):
    print("There is a tower on " + tower + ".")