print(" <비유법 퀴즈> 퀴즈는 총 5문제 입니다.\n")

      
import random

k = [["내 누님같이 생긴 꽃이여", "직유법"], ["이것은 소리 없는 아우성", "은유법"],
     ["산이 달린다", "활유법"], ["따는 밤을 새워 우는 벌레는 부끄러운 이름을 슬퍼하는 까닭입니다.", "의인법"],
     ["빈 수레가 요란하다", "풍유법"], ["비둘기만 번지가 없어졌다", "제유법"], ["흰옷 입은 소녀의 불멸의 순수(흰옷:우리 겨레)", "환유법"],
     ["하롱하롱 꽃입이 지는 어느날", "의태법"], ["수양산 바라보며 이제를 한하노라(수양산:1.중국의 수양산 2.수양대군)", "중의법"]]


quiz = True
score = 0
quiz_num = 0

for i in range(5):
    quiz_num += 1
    multi_choice = random.sample(k, 5)
    answer_index = random.randint(0, 4)

    print(f"문제{quiz_num}. '{multi_choice[answer_index][0]}'에 사용된 비유법으로 가장 알맞은 것은?")

    for i in range(5):
        print(f"{i+1}. {multi_choice[i][1]}")

    print()
    user_input = int(input(" 정답을 입력해주세요.   >>>   "))

    if user_input == answer_index + 1:
        score += 1
        print(" 정답입니다.")
        print("\n")
    else :
        print(f" 오답입니다. 정답은 {answer_index + 1}입니다. ")
        print("\n")

print("퀴즈가 종료되었습니다.")
print(f"총 {quiz_num}문제 중 {score}문제를 맞췄습니다. ")
print(f"점수는 {score}점입니다.")
