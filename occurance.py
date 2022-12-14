aSize = int(input('enter arr size: '))
print('enter arr')
a = []
counter = []
for i in range(0, aSize):
    ele = int(input())
    a.append(ele)
    counter.append(0)


bSize = int(input('enter occurance arr size: '))
print('enter occurance arr')
occ = []
for i in range(0, bSize):
    ele = int(input())
    for j in a:
        if(j == ele):
            counter[a.index(j)]+=1
    occ.append(ele)

print(counter)