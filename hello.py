import random

def play_game():
        valid_inputs = ['묵', '찌', '빠']
        user_win_count = 0
        computer_win_count = 0
        tie_count = 0

        while True:
            user_choice = input("묵, 찌, 빠 중에서 한가지를 선택해 주세요: ").lower()
            if user_choice not in valid_inputs:
                print("유효하지 않습니다")
                continue

            computer_choice = random.choice(valid_inputs)
            print(f"사용자: {user_choice}, 상대방: {computer_choice}")

            if user_choice == computer_choice:
                print("무승부!!")
                tie_count +=1
            elif (user_choice == '찌' and computer_choice == '빠') or \
                (user_choice == '묵' and computer_choice == '찌') or \
                (user_choice == '빠' and computer_choice == '묵'):
                print("나의 승리!")
                user_win_count += 1
            else:
                print("나의 패배ㅠ")
                computer_win_count +=1

            regame = input("다시 하시겠습니까? (y/n): ")
            if regame.lower() !='y':
                break

play_game()