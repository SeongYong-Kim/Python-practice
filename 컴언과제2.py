#1
list_num = int(input("enter num of list >> "))

data_list = []
result = []

for i in range(1, list_num+1):
    str = input("enter data >> ")
    data_list.append(str)

for j in range(0, len(data_list)):
    if data_list.count(data_list[j]) >= 2:
        if data_list[j] not in result:
            result.append(data_list[j])

print(result)

#2
while True:
    year = int(input("연도를 입력하세요: "))
    if year < 0:
        print("program end!")
        break
    else:
        if (year % 4) == 0 and (year % 100) != 0:
            print("{}년은 윤년입니다".format(year))
        else:
            print("{}년은 평년입니다".format(year))


#3
num = int(input("정수를 입력하세요 : "))
divisor = []

for i in range(1, num+1):
    if (num % i) == 0:
        divisor.append(i)

print("{0}의 약수는 {1}입니다.".format(num, divisor))
