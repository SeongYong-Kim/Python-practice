ary= []
d_ary= []
for  i in range(10):
    ary.append(i+10)
    print('{:3d}'.format( ary[i]), end='')
print()
for i in range(3):
    d_ary.append([])
    for j in range(4):
        d_ary[i].append(i+j)
        print('{:3d}'.format(d_ary[i][j]), end='')
    print()
