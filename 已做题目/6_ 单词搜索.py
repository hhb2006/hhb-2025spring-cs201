from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, k):
            if k == len(word) - 1:
                return True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(board) and 0 <= ny < len(board[0])
                         and (nx, ny) not in vis and board[nx][ny] == word[k + 1]):
                    vis.add((nx, ny))
                    if dfs(nx, ny, k + 1):
                        return True
                    vis.remove((nx, ny))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    vis = {(i, j)}
                    if dfs(i, j, 0):
                        return True
        return False


if __name__ == '__main__':
    print(Solution().exist(board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "B", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]], word = "AB"))