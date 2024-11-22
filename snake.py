import curses
from random import randint

def snake_game():
    # curses 초기화
    screen = curses.initscr()
    curses.curs_set(0)  # 커서 숨기기
    screen.keypad(1)  # 키패드 모드 활성화
    screen.timeout(120)  # 120ms 대기 (속도 증가)

    # 창 크기 설정
    screen_height, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_height, screen_width, 0, 0)

    # 초기 스네이크 설정
    snake = [[screen_height // 2, screen_width // 4], [screen_height // 2, screen_width // 4 - 1], [screen_height // 2, screen_width // 4 - 2]]
    direction = 'RIGHT'
    
    # 먹이 생성
    food = [randint(1, screen_height - 2), randint(1, screen_width - 2)]
    window.addch(food[0], food[1], '*')  # 먹이 표시

    score = 0

    while True:
        window.addstr(0, 2, f'Score: {score} ')  # 점수 표시

        # 사용자 입력 처리
        next_key = window.getch()
        if next_key == ord('w') and direction != 'DOWN':
            direction = 'UP'
        elif next_key == ord('s') and direction != 'UP':
            direction = 'DOWN'
        elif next_key == ord('a') and direction != 'RIGHT':
            direction = 'LEFT'
        elif next_key == ord('d') and direction != 'LEFT':
            direction = 'RIGHT'
        elif next_key == ord('q'):  # 'q' 입력 시 종료
            break

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

        snake.insert(0, new_head)

        # 스네이크가 먹이를 먹으면
        if snake[0] == food:
            score += 1
            food = [randint(1, screen_height - 2), randint(1, screen_width - 2)]
            while food in snake:  # 먹이가 스네이크와 겹치지 않도록
                food = [randint(1, screen_height - 2), randint(1, screen_width - 2)]
            window.addch(food[0], food[1], '*')
        else:
            # 먹지 않았다면 꼬리를 제거
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        # 스네이크 충돌 검사
        if (snake[0][0] in [0, screen_height] or  # 벽 충돌
            snake[0][1] in [0, screen_width] or 
            snake[0] in snake[1:]):  # 자기 자신 충돌
            break

        # 화면에 스네이크 표시
        window.addch(snake[0][0], snake[0][1], 'O')

    curses.endwin()  # curses 종료
    print(f"게임 오버! 최종 점수: {score}")

# 실행
if __name__ == "__main__":
    snake_game()
