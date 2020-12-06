def marathon(A,B):
    for i in range(len(B)):
        A.remove(B[i])
    return A[0]

p = ['a', 'a', 'c','d','e']
c = ['a', 'c', 'd', 'e']
result = marathon(p,c)
print(f'미완주자: {result}')
