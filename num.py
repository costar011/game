import random

def number_guessing_game():
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("컴퓨터가 1부터 100 사이의 숫자를 선택했습니다. 맞춰보세요!")
    
    # 컴퓨터가 무작위 숫자 선택
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            if guess < secret_number:
                print("너무 낮습니다! 다시 시도하세요.")
            elif guess > secret_number:
                print("너무 높습니다! 다시 시도하세요.")
            else:
                print(f"축하합니다! 정답은 {secret_number}입니다. {attempts}번 만에 맞추셨습니다!")
                break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

if __name__ == "__main__":
    number_guessing_game()
