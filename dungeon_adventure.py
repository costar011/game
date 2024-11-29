import random

def dungeon_exploration():
    print("=== Dungeon Exploration Game ===")
    print("당신은 어두운 던전에 갇혔습니다. 목표는 보물을 찾고 무사히 탈출하는 것입니다.")

    # 난이도 선택
    print("\n난이도를 선택하세요:")
    print("1. 쉬움 (몬스터 약함, 보물 발견 확률 높음)")
    print("2. 보통 (기본 설정)")
    print("3. 어려움 (몬스터 강함, 보물 발견 확률 낮음)")

    # 난이도 입력받기
    while True:
        difficulty = input("난이도 (1/2/3): ")  # 난이도를 입력받는 변수
        if difficulty in ["1", "2", "3"]:
            difficulty = int(difficulty)
            break
        else:
            print("올바른 숫자를 입력해주세요.")

    # 난이도 설정
    if difficulty == 1:
        health = 150  # 플레이어 초기 체력
        monster_attack_range = (5, 15)  # 몬스터 공격력 범위 (쉬움)
        treasure_probability = 0.6  # 보물 발견 확률 (쉬움)
    elif difficulty == 2:
        health = 100
        monster_attack_range = (10, 30)
        treasure_probability = 0.5
    else:
        health = 70
        monster_attack_range = (15, 40)
        treasure_probability = 0.3

    treasure = 0  # 플레이어가 모은 보물 총량
    monsters = ["Slime", "Goblin", "Dragon"]  # 등장 가능한 몬스터 목록

    # 게임 루프
    while health > 0:
        print("\n1. 앞으로 간다")
        print("2. 체력을 확인한다")
        print("3. 게임 종료")
        choice = input("선택지를 고르세요: ")  # 플레이어 선택 입력받기

        if choice == "1":
            event = random.random()  # 랜덤 이벤트 결정
            if event < treasure_probability:
                # 보물을 발견한 경우
                found_treasure = random.randint(20, 100)  # 발견한 보물의 양
                print(f"\n보물을 찾았습니다! {found_treasure} 골드를 얻었습니다.")
                treasure += found_treasure
            elif event < 0.8:
                # 몬스터와의 만남
                monster = random.choice(monsters)  # 랜덤 몬스터 선택
                attack = random.randint(*monster_attack_range)  # 몬스터의 공격력 결정
                print(f"\n몬스터 {monster}을(를) 만났습니다! 공격력이 {attack}입니다.")
                
                # 전투 여부 선택
                fight_choice = input("싸우겠습니까? (y/n): ").lower()
                if fight_choice == "y":
                    if random.random() > 0.5:
                        print(f"당신이 {monster}을(를) 물리쳤습니다!")
                        loot = random.randint(10, 50)  # 전투 후 얻는 보물
                        treasure += loot
                        print(f"추가로 {loot} 골드를 얻었습니다.")
                    else:
                        print(f"{monster}에게 공격을 받았습니다! 체력이 {attack}만큼 줄어듭니다.")
                        health -= attack
                else:
                    print(f"{monster}으로부터 도망쳤습니다. 하지만 체력이 10 감소합니다.")
                    health -= 10
            else:
                # 빈 방을 만난 경우
                print("\n아무것도 없는 빈 방입니다. 계속 탐험하세요.")
        
        elif choice == "2":
            # 현재 상태 확인
            print(f"\n현재 체력: {health}")
            print(f"현재 보유한 보물: {treasure} 골드")
        
        elif choice == "3":
            # 게임 종료
            print("\n게임을 종료합니다.")
            print(f"최종 보유한 보물: {treasure} 골드")
            print("안녕히 가세요!")
            break
        
        else:
            print("\n올바른 선택지를 입력해주세요.")
    
    if health <= 0:
        # 체력이 모두 소진된 경우 게임 오버
        print("\n체력이 모두 소진되었습니다. 게임 오버!")
        print(f"최종 보유한 보물: {treasure} 골드")

# 게임 실행
if __name__ == "__main__":
    dungeon_exploration()
