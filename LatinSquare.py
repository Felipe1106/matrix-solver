from sys import exit


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,len(bo)+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j == (len(bo) - 1):
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

if __name__ == "__main__":
    matrix = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line:
            break

        matrix.append([int(n) for n in line.split(' ')])
    solve(matrix)
    print_board(matrix)



