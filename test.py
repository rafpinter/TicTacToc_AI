"""
EMPTY = None
X = "X"
O = "O"

test = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, X, EMPTY],
        [EMPTY, EMPTY, O]]

def player(board):

    counter = 0

    for i in board:
        for j in i:
            if j != EMPTY:
                counter += 1

    if counter % 2 == 0:
        return X

    return O


def result(board, action):

    plr = player(board)

    print(plr)

    for i in range(3):
        if i == action[0]:
            for j in range(3):
                if j == action[1]:
                    board[i][j] = plr
    return board

print(result(test, (0,2)))
"""

possibo = {
    "first":4,
    "second": 2
}

possibo["third"] = 1

print(min(possibo, key=possibo.get))