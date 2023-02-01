
def showMatrix(matrix):
    return f'{matrix[0]} {matrix[1]} {matrix[2]} \n{matrix[3]} {matrix[4]} {matrix[5]} \n{matrix[6]} {matrix[7]} {matrix[8]} \n'


def checkWin(matrix):
    if matrix[0] == matrix[1] == matrix[2]:
        # print(f'Победили {matrix[0]}')
        return 1
    elif matrix[3] == matrix[4] == matrix[5]:
        # print(f'Победили {matrix[3]}')
        return 1
    elif matrix[6] == matrix[7] == matrix[8]:
        # print(f'Победили {matrix[6]}')
        return 1
    elif matrix[0] == matrix[3] == matrix[6]:
        # print(f'Победили {matrix[0]}')
        return 1
    elif matrix[1] == matrix[4] == matrix[7]:
        # print(f'Победили {matrix[1]}')
        return 1
    elif matrix[2] == matrix[5] == matrix[8]:
        # print(f'Победили {matrix[2]}')
        return 1
    elif matrix[0] == matrix[4] == matrix[8]:
        # print(f'Победили {matrix[0]}')
        return 1
    elif matrix[2] == matrix[4] == matrix[6]:
        # print(f'Победили {matrix[2]}')
        return 1
    else:
        return 0
