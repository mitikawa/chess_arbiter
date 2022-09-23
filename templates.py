import cv2

white_king = cv2.imread('static/white_king.png')
white_queen = cv2.imread('static/white_queen.png')
white_rook = cv2.imread('static/white_rook.png')
white_knight = cv2.imread('static/white_knight.png')
white_bishop = cv2.imread('static/white_bishop.png')
white_pawn = cv2.imread('static/white_pawn.png')

black_king = cv2.imread('static/black_king.png')
black_queen = cv2.imread('static/black_queen.png')
black_rook = cv2.imread('static/black_rook.png')
black_knight = cv2.imread('static/black_knight.png')
black_bishop = cv2.imread('static/black_bishop.png')
black_pawn = cv2.imread('static/black_pawn.png')


mask_king = cv2.imread('static/mask_king.png')
mask_queen = cv2.imread('static/mask_queen.png')
mask_rook = cv2.imread('static/mask_rook.png')
mask_knight = cv2.imread('static/mask_knight.png')
mask_bishop = cv2.imread('static/mask_bishop.png')
mask_pawn = cv2.imread('static/mask_pawn.png')



templates = {'white_king':[white_king,mask_king],
'white_queen':[white_queen,mask_queen],
'white_rook':[white_rook,mask_rook],
'white_knight':[white_knight,mask_knight],
'white_bishop':[white_bishop,mask_bishop],
'white_pawn':[white_pawn,mask_pawn],
'black_king':[black_king,mask_king],
'black_queen':[black_queen,mask_queen],
'black_rook':[black_rook,mask_rook],
'black_knight':[black_knight,mask_knight],
'black_bishop':[black_bishop,mask_bishop],
'black_pawn':[black_pawn,mask_pawn]}