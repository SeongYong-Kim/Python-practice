def list_sorting(list,index):
    criteria = []
    result = []
    for i in range(len(list)):
        criteria.append(list[i][index])
    criteria.sort()
    for n in range(len(criteria)):
        for m in range(len(list)):
            if criteria[n] == list[m][index]:
                result.append(list[m])

    return result

list = []

while True:
    size = int(input("생성할 string의 개수를 입력하세요 >> "))
    if size > 10 or size < 3:
        print("string의 개수가 너무 많거나 작습니다")
        print("")
    else:
        break

for i in range(size):
    string = input("string >> ")
    if len(string) > 30 or len(string) < 2:
        print("string의길이가 너무 길거나 짧습니다")
        print("지금 입력된 string은 사용되지 않습니다")
        print("")
    else:
        list.append(string)

index = int(input("input index >> "))

sorted = list_sorting(list,index)
print(sorted)
