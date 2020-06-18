
class ConnectGame:
    def __init__(self, board):
        self.board = board

    def get_winner(self):
        board = [s.replace(' ', '') for s in self.board.splitlines()]
        w,h = len(board[0]), len(board)
        board = {q + 1j * r: x for r,row in enumerate(board) for q,x in enumerate(row)}
        moves = [-1j, 1j, -1, 1, 1-1j, -1+1j]

        def find_path(player, fro, toany):
            fringe = [fro]
            visited = set()

            while fringe:
                pos = fringe.pop()

                if pos in toany:
                    return True

                if pos in visited:
                    continue
                visited.add(pos)

                for move in moves:
                    x = pos + move
                    if board.get(x, None) == player:
                        fringe.append(x)
            return False

        def any_path(player, fro, to):
            return any(find_path(player, x, to) for x in fro)

        def xqs(q):
            return {k for k,v in board.items() if v == 'X' and k.real == q}

        def ors(r):
            return {k for k,v in board.items() if v == 'O' and k.imag == r}

        xwins = any_path('X', xqs(0), xqs(w - 1))
        owins = any_path('O', ors(0), ors(h - 1))

        return 'O' if owins else 'X' if xwins else ''
