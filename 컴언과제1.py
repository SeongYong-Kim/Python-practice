#1
hour = 0
minute = 0
second = 0

seconds = int(input("Enter seconds >> "))
hour = seconds // 3600
minute = (seconds % 3600) // 60
second = (seconds % 3600) % 60

print("{0}시간 {1}분 {2}초".format(hour,minute,second))

#2
print("임진왜란은\n1592년('선조 25년')부터\n1598년까지 2차에 걸친\n'왜군의 침략'으로\n일어난 전쟁이다. ")

#3
num1 = int(input("첫번째 정수 입력>> "))
num2 = int(input("두번째 정수 입력>> "))
print("덧셈, 뺄셈, 곱셈, 나눗셈, 나누기의 몫, 나누기의 나머지 계산 ")
print("{:.0f}  + {:6.0f} = {:11.0f}".format(num1, num2, num1+num2))
print("{:.0f}  - {:6.0f} = {:11.0f}".format(num1, num2, num1-num2))
print("{:.0f}  * {:6.0f} = {:11.0f}".format(num1, num2, num1*num2))
print("{:.0f}  / {:6.0f} = {:11.3f}".format(num1, num2, num1/num2))
print("{:.0f}  / {:6.0f}의 몫 : {:6.0f}".format(num1, num2, num1//num2))
print("{:.0f}  / {:6.0f}의 나머지 : {:2.0f}".format(num1, num2, num1%num2))
#.찍는 순간 필드폭 생략가능, 정밀도 생략 불가능

#4
num = float(input("실수값 입력>> "))
print("{0}은 정수{1:d}와 소수점 이하 {2:g}로 구성".format(num, int(num), num-int(num)))

#5
strr = str(input("Enter alphabet>> "))
strr = strr.lower()

str_list = []

for i in range(len(strr)):
    str_list.append(strr[i])

str_set = []

for n in str_list:
    if n not in str_set:
        str_set.append(n)

counter = []

for j in range(len(str_set)):
    counter.append(str(strr.count(str_set[j])))

for k in range(len(str_set)):
    print(str_set[k] + counter[k], end ='')
