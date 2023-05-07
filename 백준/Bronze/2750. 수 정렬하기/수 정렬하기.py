N=int(input())
my=[]
for i in range(N):
    my.append(int(input()))
for i in range(N-1):
    for j in range(N-1-i):
        if my[j]>my[j+1]:
            tmp=my[j]
            my[j]=my[j+1]
            my[j+1]=tmp

for i in range(len(my)):
    print(my[i])