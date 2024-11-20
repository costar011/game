import curses
from random import randint

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
    direction = 'RIGHT'
    key_map = {
        'w': 'UP',
        's': 'DOWN',
        'a': 'LEFT',
        'd': 'RIGHT'
    }

    # 먹이 생성
    food = [randint(1, screen_height-2), randint(1, screen_width-2)]
    window.addch(food[0], food[1], '*')

    # 점수 초기화
    score = 0

    while True:
        # 점수 표시
        window.addstr(0, 2, f"Score: {score} ")

        # 사용자 입력 처리
        try:
            next_key = window.getkey()
            if next_key in key_map:
                direction = key_map[next_key]
            elif next_key == 'KEY_LEFT':  # 터미널에서 방향키 처리
                direction = 'LEFT'
            elif next_key == 'KEY_RIGHT':
                direction = 'RIGHT'
            elif next_key == 'KEY_UP':
                direction = 'UP'
            elif next_key == 'KEY_DOWN':
                direction = 'DOWN'
        except curses.error:
            pass

        # 스네이크 머리 이동
        head = snake[0]
        if direction == 'RIGHT':
            new_head = [head[0], head[1] + 1]
        elif direction == 'LEFT':
            new_head = [head[0], head[1] - 1]
        elif direction == 'UP':
            new_head = [head[0] - 1, head[1]]
        elif direction == 'DOWN':
            new_head = [head[0] + 1, head[1]]
        else:
            new_head = head  # 유효하지 않은 방향은 무시

        snake.insert(0, new_head)

        # 스네이크가 먹이를 먹으면
        if snake[0] == food:
            score += 1
            food = [randint(1, screen_height-2), randint(1, screen_width-2)]
            window.addch(food[0], food[1], '*')
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
        window.addch(snake[0][0], snake[0][1], 'O')

    curses.endwin()
    print(f"게임 오버! 최종 점수: {score}")

# 실행
if __name__ == "__main__":
    snake_game()
