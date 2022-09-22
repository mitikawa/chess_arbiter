import cv2
import numpy as np

board_img = cv2.imread('static/board_with_king.png')
king_img = cv2.imread('static/king_on_white_background.jpg')

result = cv2.matchTemplate(board_img, king_img,cv2.TM_CCOEFF_NORMED)

_, _, _, max_loc = cv2.minMaxLoc(result)

king_int_coordinates = (max_loc[0]//73,max_loc[1]//73)
columns = 'abcdefgh'
king_square = columns[king_int_coordinates[0]]+str(8-king_int_coordinates[1])

print(king_square)

