x = int(input('enter x: '))
sum = 0
for i in range(1, x+1):
    sum+=i
    if(sum % x == 0):
        print(sum)