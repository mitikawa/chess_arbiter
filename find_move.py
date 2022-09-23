import cv2
import numpy as np

board_img = cv2.imread('static/board_with_two_towers.png')
board_img_after_move = cv2.imread('static/board_rf1_rb4.png')
board_img_illegal_move = cv2.imread('static/board_illegal_rook_move.png')
board_img_simultaneous_moves = cv2.imread('static/board_simultaneous_moves.png')

tower_template = cv2.imread('static/tower_grey.png')
threshold = 0.8
square_pixel_size = int(board_img.shape[0]/8)

def init_board_dict():
    board_dict = {}
    for i in range(0,8):
        for j in range(0,8):
            board_dict[(i,j)]=0
    return board_dict

def get_square_name(coordinates):
    columns = 'abcdefgh'
    square = columns[coordinates[0]]+str(8-coordinates[1])
    return square

def find_tower(board_img, template=tower_template,method=cv2.TM_CCOEFF_NORMED, threshold = threshold, board=None):
    if board==None:
        board=init_board_dict()
    match_template_result = cv2.matchTemplate(board_img, template, method)
    ys,xs = np.where(match_template_result>=threshold)
    for i in range(len(xs)):
        board[(xs[i]//square_pixel_size,ys[i]//square_pixel_size)] = 'tower'
    return board

def find_tower_move(original_board, next_board):
    comparison_dict={}
    for key, _ in original_board.items():
        if original_board[key] != next_board[key]:
            if original_board[key]!=0:
                comparison_dict[key] = 'original_position'
            else:
                comparison_dict[key] = 'next_position'
    return comparison_dict


def check_move(original_img,next_img):
    original_board = find_tower(original_img)
    next_board = find_tower(next_img)
    board_comparison = find_tower_move(original_board, next_board)
    if len(board_comparison)>2:
        print("More than one move found.")
        return
    if len(board_comparison)==0:
        print('No move found.')
        return
    original_coordinates = [k for k,v in board_comparison.items() if v=='original_position'][0]
    next_coordinates = [k for k,v in board_comparison.items() if v=='next_position'][0]
    if original_coordinates[0]!=next_coordinates[0] and original_coordinates[1]!=next_coordinates[1]:
        print('Illegal tower move: ' + get_square_name(original_coordinates) + ' -> ' + get_square_name(next_coordinates))
        return
    print('Valid tower move: ' + get_square_name(original_coordinates) + ' -> ' + get_square_name(next_coordinates))
    



check_move(board_img, board_img_after_move)
check_move(board_img, board_img_illegal_move)
check_move(board_img, board_img_simultaneous_moves)
check_move(board_img, board_img)