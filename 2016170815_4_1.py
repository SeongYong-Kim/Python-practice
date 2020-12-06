import random as rd

def del_minimum(original_list):
    num = len(original_list)
    min = 100

    for j in range(num):
        if original_list[j] < min:
            min = original_list[j]

    original_list.remove(min)
    after_deletion = original_list

    if len(after_deletion) == 0:
        after_deletion.append(-1)
        return after_deletion

    return after_deletion

#main code
while True:
    num = int(input("Enter the number of lists >> "))
    if num <= 10 and num >= 1:
        break
    print("Wrong number")
    print("")

original_list = [rd.randrange(1, 101) for i in range(num)]
print("original list :", original_list)

after_deletion = del_minimum(original_list)
print("after deletion :", after_deletion)
