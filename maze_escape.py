import os
import random

# DFS를 사용한 미로 생성
def generate_maze(width, height):
    # 초기 미로는 모두 벽으로 채움
    maze = [["#" for _ in range(width)] for _ in range(height)]

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # DFS로 미로 생성
    def carve(x, y):
        maze[x][y] = " "  # 현재 위치를 빈 공간으로 설정
        random.shuffle(directions)  # 랜덤한 방향으로 진행
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # 두 칸씩 이동
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx][ny] == "#":
                maze[x + dx][y + dy] = " "  # 중간 칸도 빈 공간으로 설정
                carve(nx, ny)  # 재귀적으로 다음 칸 탐색

    # 시작 위치를 랜덤으로 설정하고 DFS 실행
    start_x, start_y = 1, 1
    carve(start_x, start_y)

    # 시작점과 탈출구 설정
    maze[start_x][start_y] = "P"  # 플레이어 시작 위치
    maze[height - 2][width - 2] = "E"  # 탈출구 위치
    return maze

# 미로 출력
def print_maze(maze):
    os.system('cls' if os.name == 'nt' else 'clear')  # 터미널 화면을 지움
    for row in maze:
        print("".join(row))

# 플레이어의 현재 위치 찾기
def find_player(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "P":  # 플레이어의 위치를 찾으면 반환
                return i, j

# 플레이어 이동
def move_player(maze, direction):
    x, y = find_player(maze)  # 현재 플레이어 위치
    new_x, new_y = x, y  # 이동 후 좌표 초기값
    if direction == "w":  # 위로 이동
        new_x -= 1
    elif direction == "s":  # 아래로 이동
        new_x += 1
    elif direction == "a":  # 왼쪽으로 이동
        new_y -= 1
    elif direction == "d":  # 오른쪽으로 이동
        new_y += 1

    # 이동 가능한지 확인
    if maze[new_x][new_y] in (" ", "E"):  # 빈 공간 또는 탈출구일 경우
        maze[x][y] = " "  # 이전 위치를 빈 공간으로 변경
        maze[new_x][new_y] = "P"  # 새로운 위치에 플레이어 설정
        return True
    return False  # 이동 불가능하면 False 반환

# 게임 실행
def play_game():
    while True:  # 무한 루프를 통해 랜덤 미로를 계속 생성
        width = random.randint(10, 20)  # 미로의 너비를 랜덤 설정
        height = random.randint(5, 10)  # 미로의 높이를 랜덤 설정
        maze = generate_maze(width, height)  # DFS 기반 미로 생성
        while True:
            print_maze(maze)  # 미로 출력
            print("W: 위로 이동, S: 아래로 이동, A: 왼쪽으로 이동, D: 오른쪽으로 이동, Q: 종료")
            move = input("이동 방향을 입력하세요: ").lower()
            if move == "q":  # 게임 종료 조건
                print("게임 종료!")
                return
            if move in ("w", "a", "s", "d"):  # 이동 입력 처리
                if not move_player(maze, move):  # 이동 실패 시
                    print("벽에 막혔습니다!")
            else:
                print("잘못된 입력입니다! W, A, S, D 중 하나를 입력하세요.")

            # 플레이어가 탈출구에 도달했는지 확인
            if maze[height - 2][width - 2] == "P":  # 탈출구 위치에 플레이어가 있으면 승리
                print_maze(maze)
                print("축하합니다! 미로를 탈출했습니다!")
                break

if __name__ == "__main__":
    play_game()
