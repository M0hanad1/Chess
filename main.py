from src.pieces.knight import Knight


test = Knight([7, 7], [[1, 2]], 'white')
test1 = Knight([6, 5], [[]], 'black')
print(test.pieces)
print(test1.board)
test.remove_piece()
del test

print(test1.pieces)
print(test1.board)
