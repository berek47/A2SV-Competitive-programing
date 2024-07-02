class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]: 
        EMPTY = "E"; MINE = "M" ;BLANK = "B"; BOOM = "X"
        rows = len(board)
        if rows == 0: return board
        cols = len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue = deque()
        queue.append(click)
        while queue:
            row, col = queue.popleft()
            if board[row][col] == MINE:
                board[row][col] = BOOM
                return board
            elif board[row][col] == EMPTY:
                adjacent_squares = []
                mine_count = 0
                for direction in DIRECTIONS:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    
                    if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols or (board[new_row][new_col] != EMPTY and board[new_row][new_col] != MINE):
                        continue
                    elif board[new_row][new_col] == MINE:
                        mine_count += 1
                    adjacent_squares.append([new_row, new_col])
                if mine_count == 0:
                    board[row][col] = BLANK
                    queue.extend(adjacent_squares)
                else:
                    board[row][col] = str(mine_count)
                    
        return board
