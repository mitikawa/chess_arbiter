import cv2

square_pixel_size = 73

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

