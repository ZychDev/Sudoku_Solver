board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def print_board(boa):
    
    for i in range(len(boa)):

        if i % 3 == 0 and i != 0 :
            print("- - - - - - - - - - - - - ")
    
        for j in range(len(boa[0])):

            if j % 3 == 0 and j != 0:
                print(" | ",end ="")

            if j == 8:
                print(str(boa[i][j]))

            else:
                print(str(boa[i][j]) + " ", end="")

            
def find_zero(boa):
    for x in range(len(boa)):
        for y in range(len(boa[0])):
            if boa[x][y] == 0:
                return (x,y)


print_board(board)
print(find_zero(board))
