import cv2
import numpy as np

board_status = cv2.imread('static/board_with_king.png')
board_valid_move = cv2.imread('static/board_valid_move.jpg')
board_illegal_move = cv2.imread('static/board_illegal_move.jpg')
king_template = cv2.imread('static/king_on_white_background.jpg')
square_pixel_size = int(board_status.shape[0]/8)

def find_king(board, template=king_template,method=cv2.TM_CCOEFF_NORMED):
    match_template_result = cv2.matchTemplate(board, template,method)
    _, _, _, max_loc = cv2.minMaxLoc(match_template_result)
    return (max_loc[0]//square_pixel_size,max_loc[1]//square_pixel_size)

def get_square_name(coordinates):
    columns = 'abcdefgh'
    square = columns[coordinates[0]]+str(8-coordinates[1])
    return square

def check_king_move(original_coordinate, next_coordinate):
    # King moved to a non-neighboring square
    if abs(original_coordinate[0]-next_coordinate[0])>1 or abs(original_coordinate[1]-next_coordinate[1])>1:
        print(get_square_name(original_coordinate) + "->" + get_square_name(next_coordinate) + " is an illegal king move.")
        return 1
    # King did not move
    elif abs(original_coordinate[0]-next_coordinate[0])==0 and abs(original_coordinate[1]-next_coordinate[1])==0:
        print("The king did not move.")
        return 1

    # King moved to a neighboring square
    print(get_square_name(original_coordinate) + "->" + get_square_name(next_coordinate) + " is a valid king move.")
    return 0 


original_king   = find_king(board_status)
valid_king      = find_king(board_valid_move)
illegal_king    = find_king(board_illegal_move)

check_king_move(original_king, original_king)
check_king_move(original_king, valid_king)
check_king_move(original_king, illegal_king)


