    # 랜덤숫자 출력
    # 사용자 값 입력
    # 정답일 때 까지 비교
    # 정답이면 종료

import random

count = 0
random_number = random.randint(1, 100)


while True:
    try:
        count = count + 1
        user_input = int(input("숫자를 입력하세요: "))


        if random_number < user_input:
            print('다운')

        elif random_number > user_input:
            print('업')

        else:
            print("정답!",count,"번 만에 맞췄습니다")
            will_continue = (input('함 더?(Y/N): '))
            if will_continue.upper() == 'Y':
                continue
            else:
                break

    except ValueError:
        print('1~100 사이의 숫자를 입력해주세요.')

