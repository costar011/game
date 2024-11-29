import random  # 난수를 생성하기 위한 random 모듈 임포트

def number_guessing_game():
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")  # 게임 환영 메시지 출력
    print("게임 시작 전에 난이도를 선택해주세요:")  # 난이도 선택 안내 메시지
    print("1. 쉬움 (1~50)")  # 쉬운 난이도 옵션
    print("2. 보통 (1~100)")  # 보통 난이도 옵션
    print("3. 어려움 (1~200)")  # 어려운 난이도 옵션

    # 난이도 설정
    while True:  # 올바른 난이도를 선택할 때까지 반복
        try:
            level = int(input("난이도를 선택하세요 (1, 2, 3): "))  # 난이도 입력 받기
            if level == 1:  # 쉬움 선택 시
                max_number = 50  # 숫자 범위를 1~50으로 설정
                break
            elif level == 2:  # 보통 선택 시
                max_number = 100  # 숫자 범위를 1~100으로 설정
                break
            elif level == 3:  # 어려움 선택 시
                max_number = 200  # 숫자 범위를 1~200으로 설정
                break
            else:  # 입력 값이 1, 2, 3이 아닐 경우
                print("1, 2, 3 중 하나를 선택해주세요.")  # 오류 메시지 출력
        except ValueError:  # 숫자가 아닌 값 입력 시 예외 처리
            print("숫자를 입력해주세요.")  # 숫자를 입력하라는 메시지 출력

    print(f"\n컴퓨터가 1부터 {max_number} 사이의 숫자를 선택했습니다. 맞춰보세요!")  # 게임 시작 메시지
    
    # 컴퓨터가 무작위 숫자 선택
    secret_number = random.randint(1, max_number)  # 선택된 난이도에 맞는 범위 내에서 숫자 선택
    attempts = 0  # 시도 횟수 초기화

    # 숫자 맞추기 루프
    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))  # 사용자로부터 숫자 입력 받기
            if guess < 1 or guess > max_number:  # 입력 값이 범위를 벗어났을 경우
                print(f"숫자는 1에서 {max_number} 사이여야 합니다.")  # 범위 오류 메시지 출력
                continue  # 다시 입력받기

            attempts += 1  # 시도 횟수 증가

            if guess < secret_number:  # 입력 값이 정답보다 작은 경우
                print("너무 낮습니다! 다시 시도하세요.")  # 힌트 메시지 출력
            elif guess > secret_number:  # 입력 값이 정답보다 큰 경우
                print("너무 높습니다! 다시 시도하세요.")  # 힌트 메시지 출력
            else:  # 정답을 맞췄을 경우
                print(f"축하합니다! 정답은 {secret_number}입니다. {attempts}번 만에 맞추셨습니다!")  # 성공 메시지 출력
                break  # 게임 종료
        except ValueError:  # 숫자가 아닌 값 입력 시 예외 처리
            print("유효한 숫자를 입력하세요.")  # 유효한 숫자를 입력하라는 메시지 출력

if __name__ == "__main__":  # 스크립트가 직접 실행될 경우에만 동작
    number_guessing_game()  # 숫자 맞추기 게임 시작
