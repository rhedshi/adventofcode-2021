#!/usr/bin/env python3

from typing import List, Tuple


class Board:
    board: List[List[int]]

    marked_rows: List[List[int]]
    marked_columns: List[List[int]]

    def __init__(self) -> None:
        self.board = []

        self.marked_rows = []
        self.marked_columns = []

        return

    def add(self, row: List[int]) -> None:
        self.board.append(row)

        self.marked_rows.append([1] * len(row))

        for i in range(len(row)):
            try:
                self.marked_columns[i].append(1)
            except IndexError:
                self.marked_columns.append([1])

        return

    def find(self, number: int) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == number:
                    self.mark(i, j)
                    return True
        return False

    def mark(self, row: int, column: int) -> None:
        self.marked_rows[row][column] = 0
        self.marked_columns[column][row] = 0
        return

    def score(self) -> int:
        result = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                result += self.board[i][j] * self.marked_rows[i][j]
        return result

    def check(self) -> bool:
        return self._check_rows() or self._check_columns()

    def _check_rows(self) -> bool:
        return any(map(lambda row: sum(row) == 0, self.marked_rows))

    def _check_columns(self) -> bool:
        return any(map(lambda column: sum(column) == 0, self.marked_columns))


def get_input() -> Tuple[List[int], List[Board]]:
    numbers = list(map(int, input().split(",")))
    boards = []

    while True:
        try:
            row = input() 

            if row == "":
                boards.append(Board())
                continue

            boards[-1].add(list(map(int, filter(None, row.split(" ")))))

        except EOFError:
            break

    return numbers, boards


numbers, boards = get_input()
score = 0
winners = set()

for number in numbers:
    for board in boards:
        if board in winners:
            continue
        board.find(number)
        if board.check():
            score = board.score() * number
            winners.add(board)

    if len(winners) == len(boards):
        break

print(score)

# Answer: 26936
