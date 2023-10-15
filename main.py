def isSafe(matrix, r, c):
    for i in range(r):
        if matrix[i][c] == 'Q':
            return False

    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if matrix[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    (i, j) = (r, c)
    while i >= 0 and j < len(matrix):
        if matrix[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def nQueen(matrix, r):
    if r == len(matrix):
        solution(matrix=matrix)
        return

    for i in range(len(matrix)):

        if isSafe(matrix, r, i):
            matrix[r][i] = 'Q'

            nQueen(matrix, r + 1)

            matrix[r][i] = '–'


def solution(matrix):
    for r in matrix:
        print(str(r).replace(',', '').replace('\'', ''))
    print()


if __name__ == '__main__':
    N = 5

    matrix = [['–' for x in range(N)] for y in range(N)]

    nQueen(matrix, 0)