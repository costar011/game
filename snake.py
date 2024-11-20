import curses
from random import randint

# 스네이크 게임 함수
def snake_game():
    # curses 초기화
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    screen.timeout(100)

    # 창 크기 설정
    screen_height, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_height, screen_width, 0, 0)

    # 초기 스네이크 설정
    snake = [[10, 15], [10, 14], [10, 13]]
    direction = curses.KEY_RIGHT

    # 먹이 생성
    food = [screen_height//2, screen_width//4]
    window.addch(food[0], food[1], curses.ACS_PI)

    while True:
        # 사용자 입력 처리
        next_key = window.getch()
        if next_key != -1:
            direction = next_key

        # 스네이크 머리 이동
        head = snake[0]
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        else:
            new_head = head  # 유효하지 않은 방향은 무시

        snake.insert(0, new_head)

        # 스네이크가 먹이를 먹으면
        if snake[0] == food:
            food = [randint(1, screen_height-1), randint(1, screen_width-1)]
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            # 먹지 않았다면 꼬리를 제거
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        # 스네이크 충돌 검사
        if (
            snake[0][0] in [0, screen_height] or  # 벽 충돌
            snake[0][1] in [0, screen_width] or  # 벽 충돌
            snake[0] in snake[1:]                # 자기 자신 충돌
        ):
            break

        # 화면에 스네이크 표시
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

    curses.endwin()
    print("게임 오버!")

# 실행
if __name__ == "__main__":
    snake_game()
