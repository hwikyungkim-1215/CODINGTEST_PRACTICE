List = {
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
}

def numIslands(self, grid: List[List[str]]) -> int:

    def dfs(i, j):
        # 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return

        # 이미 방문한 곳은 #으로 마킹
        grid[i][j] = '#'
        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # 육지인 경우
            if grid[i][j] == '1':
                # 탐색
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    return count

print(numIslands(self))