"""
문제 : 바탕화면 정리

컴퓨터 바탕화면 상태를 나타낸 문자열 배열 wallpapaer

파일들은 바탕화면의 격자칸에 위치하고 바탕화면의 격자점들은 
바탕화면의 가장 왼쪽 위를 (0, 0)으로 시작해 (세로 좌표, 가로 좌표)로 표현합니다.
빈칸은 ".", 파일이 있는 칸은 "#"의 값을 가집니다.

드래그를 하면 파일들을 선택할 수 있고, 선택된 파일들을 삭제할 수 있습니다. 

최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일을 선택해서 한 번에 지우려고 하며 드래그로 파일들을 선택하는 방법은 다음과 같습니다.

드래그는 격자점 S(lux,luy)를 왼클릭 상태로 E(rdx,rdy)로 이동한뒤 버튼을 떼는 행동.

S  = 시작점
E = 끝점
드래그한 거리 = | rdx - lux | + |rdy -luy| 

wallpaper = [".#...", "..#..", "...#."]
그림과 같이 S(0, 1)에서 E(3, 4)로 드래그하면 
세 개의 파일이 모두 선택되므로 드래그 한 거리 (3 - 0) + (4 - 1) = 6을 최솟값으로 모든 파일을 선택 가능

최소한의 이동거리를 갖는 드래그의 시작점과 끝점을 담은 정수 배열을 return
드래그의 시작점이 (lux, luy), 끝점이 (rdx, rdy)라면 정수 배열 [lux, luy, rdx, rdy]를 return하면 됩니다.
"""


a = [".#...", "..#..", "...#."]
b = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
c = [
    ".##...##.",
    "#..#.#..#",
    "#...#...#",
    ".#.....#.",
    "..#...#..",
    "...#.#...",
    "....#....",
]
d = ["..", "#."]


# lux,luy 는 최소값
# rdx,rdy 는 최대값


# re활용 무작위 풀이
import re


def solve(i):
    res = [None, None, None, None]
    file_icon = "#"
    for i, v in enumerate(i):
        if file_icon in v:
            if res[0] is None:
                res[0] = i
            res[2] = i + 1
            files = [f.start() for f in re.finditer(file_icon, v)]
            if res[1] is None:
                res[1] = files[0]
                res[3] = files[-1] + 1
            else:
                if len(files) > 1:
                    if res[1] > files[0]:
                        res[1] = files[0]
                    if res[3] <= files[-1]:
                        res[3] = files[-1] + 1
                elif len(files) == 1:
                    if res[3] <= files[-1]:
                        res[3] = files[-1] + 1
    return res


# 최적화
def solve(wallpaper):
    min_row, min_col = float("inf"), float("inf")  # 가장 큰 수
    max_row, max_col = 0, 0
    file_exist_icon = "#"
    for i, v in enumerate(wallpaper):
        for j, cha in enumerate(v):
            if cha == file_exist_icon:
                min_row = min(min_row, i)
                max_row = max(max_row, i + 1)

                min_col = min(min_col, j)
                max_col = max(max_col, j + 1)

    res = [min_row, min_col, max_row, max_col]
    return res


solve(a)
solve(b)
solve(c)
solve(d)
