def minMoves(n, startRow, startCol, endRow, endCol):
    directions = [[2,1], [2,-1], [-2, 1], [-2, -1], [1,2], [1,-2], [-1,2], [-1,-2]]

    visited = [[False]*(n) for _ in range(n)]

    #queue will store [row,col,steps]
    queue = [[startRow, startCol, 0]]
    while queue:
        row, col, moves = queue.pop(0)
        if [row, col] == [endRow, endCol]:
            return moves
        for dx, dy in directions:
            bounds = (0 <= row + dx < n and 0 <= col + dy < n)
            if bounds and not visited[row + dx][col + dy]:
                visited[row + dx][col + dy] = True
                queue.append([row + dx, col + dy, moves + 1])
    return -1
