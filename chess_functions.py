import cv2
from templates import templates
import numpy as np

square_pixel_size = 73
threshold = 0.9

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

def recognize_pieces(board_img, templates=templates,method=cv2.TM_CCORR_NORMED , threshold = threshold, board=None):
    if board==None:
        board=init_board_dict()
    for piece in templates:
        match_template_result = cv2.matchTemplate(board_img, templates[piece][0], method, mask = templates[piece][1])
        ys,xs = np.where(match_template_result>=threshold)
        for i in range(len(xs)):
            if board[(xs[i]//square_pixel_size,ys[i]//square_pixel_size)] == 0:
                board[(xs[i]//square_pixel_size,ys[i]//square_pixel_size)] = f"{piece}"
    return board

def find_move(original_board, next_board):
    comparison_dict={}
    for key, _ in original_board.items():
        if original_board[key] != next_board[key]:
            if original_board[key]!=0:
                comparison_dict[key] = ['original_position', original_board[key]]
            else:
                comparison_dict[key] = ['next_position', next_board[key]]
    return comparison_dict

def get_x_y_coord_and_name(original_coordinates,next_coordinates):
    x_0, y_0, x_1, y_1 = original_coordinates[0], original_coordinates[1], next_coordinates[0], next_coordinates[1]
    x,y = get_square_name(original_coordinates), get_square_name(next_coordinates)
    return x,y,x_0,y_0,x_1,y_1

def check_move(comparison_dict):
    if len(comparison_dict)>2:
        print("More than one move found.")
        print('-----------------------------------------------')
        return
    if len(comparison_dict)==0:
        print('No move found.')
        print('-----------------------------------------------')
        return
    original_coordinates = [k for k,v in comparison_dict.items() if v[0]=='original_position'][0]
    next_coordinates = [k for k,v in comparison_dict.items() if v[0]=='next_position'][0]
    piece = comparison_dict[original_coordinates][1]
    if piece =='white_pawn' or piece=='black_pawn':
        check_pawn_move(original_coordinates, next_coordinates, piece)
    if piece in ('black_rook','white_rook'):
        check_rook_move(original_coordinates, next_coordinates, piece)
    if piece in ('black_bishop', 'white_bishop'):
        check_bishop_move(original_coordinates, next_coordinates, piece)
    if piece in ('black_king','white_king'):
        check_king_move(original_coordinates, next_coordinates, piece)


def check_pawn_move(original_coordinates,next_coordinates,piece):
    x,y,x_0,y_0,x_1,y_1 = get_x_y_coord_and_name(original_coordinates,next_coordinates)
    if piece=='white_pawn':
        if x_0!=x_1:
            print('Illegal white pawn move: ' + x + ' -> ' + y)
            print('Attention: en passant and capture rules are not implemented')
            print('-----------------------------------------------')
            return
        if y_0<y_1:
            print('Illegal pawn move backwards: ' + x + ' -> ' + y)
            print('-----------------------------------------------')
            return
        if y_0-y_1>2:
            print('Pawns cannot move more than 2 squares at once. '+ x + ' -> ' + y)
            print('-----------------------------------------------')
            return
        if y_0-y_1 == 2 and not y_0 == 6:
            print('Pawns cannot move 2 squares if not on original rank. '+ x + ' -> ' + y)
            print('-----------------------------------------------')
            return
        print('Valid pawn move: '+ x + ' -> ' + y)
        print('-----------------------------------------------')
        return
    if piece=='black_pawn':
        if x_0!=x_1:
            print('Illegal black pawn move: ' + x + ' -> ' + y)
            print('Attention: en passant and capture rules are not implemented')
            print('-----------------------------------------------')
            return
        if y_0>y_1:
            print('Illegal pawn move backwards: ' + x + ' -> ' + y)
            print('-----------------------------------------------')
            return
        if y_1-y_0>2:
            print('Pawns cannot move more than 2 squares at once. '+ x + ' -> ' + y)
            print('-----------------------------------------------')
            return
        if y_1-y_0 == 2 and not y_0 == 1:
            print('Pawns cannot move 2 squares if not on original rank. '+ x + ' -> ' + y)
            print('-----------------------------------------------')
            return
        print('Valid pawn move: '+ x + ' -> ' + y)
        print('-----------------------------------------------')
        return


def check_rook_move(original_coordinates, next_coordinates, piece):
    x,y,x_0,y_0,x_1,y_1 = get_x_y_coord_and_name(original_coordinates,next_coordinates)
    if x_0!=x_1 and y_0!=y_1:
        print('Illegal rook move: ' + x + ' -> ' + y)
        return
    print('Valid rook move: '+ x + ' -> ' + y)

def check_bishop_move(original_coordinates, next_coordinates, piece):
    x,y,x_0,y_0,x_1,y_1 = get_x_y_coord_and_name(original_coordinates,next_coordinates)
    if abs(x_0-x_1) != abs(y_0-y_1):
        print('Illegal bishop move: ' + x + ' -> ' + y)
        return
    print('Valid bishop move: '+ x + ' -> ' + y)


def check_king_move(original_coordinates, next_coordinates, piece):
    x,y,x_0,y_0,x_1,y_1 = get_x_y_coord_and_name(original_coordinates,next_coordinates)
    if abs(x_0-x_1)>1 or abs(y_0-y_1)>1:
        print('Illegal king move: ' + x + ' -> ' + y)
        return
    print('Valid king move: ' + x + ' -> ' + y)
