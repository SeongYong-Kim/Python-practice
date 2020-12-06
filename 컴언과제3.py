#3-1
import random as rd

user_input = []
answer = rd.randrange(1,31)

for i in range(3):
    num = int(input("1~30의 정수값을 입력하세요>> "))
    user_input.append(num)

    if num == answer:
        print("You Win!!")
        print("")
        break
    if num > answer:
        print("Your number is bigger than answer")
        print("")
    if num < answer:
        print("Your number is smaller than answer")
        print("")

if len(user_input) == 3 and user_input[2] != answer:
    print("You lose!!")
    print("")

print("Your numbers :", user_input)
print("Answer :", answer)

#3-2
dic = {'A':90, 'B':80}

while True:
    switch = int(input("start(1) or stop(0) : "))

    if switch == 1:
        key = input("Please enter a key to search, ex)C,D>> ")
        if key in dic.keys():
            print("{}의 값은".format(key), dic[key])
            print("딕셔너리 ::", dic)
            print("")
        else:
            print("찾는 키가 없습니다. 딕셔너리에 추가할 값을 입력하세요")
            new = input("{}에 해당되는 값 입력 :: ".format(key))
            dic.update({key : new})
            print("딕셔너리 ::", dic)
            print("")
    else:
        print("program end")
        break

#3-3
while True:
    str = input("단어를 입력하세요: ")
    list = []
    list_inverse = []
    for i in range(len(str)):
        list.append(str[i])
    for j in range(-1, -(len(str)+1), -1):
        list_inverse.append(str[j])

    if str == "quit":
        print("program end...")
        break
    else:
        if list == list_inverse:
            print("{} is palindrome".format(str))
            print("")
        else:
            print("{} is not palindrome".format(str))
            print("")
