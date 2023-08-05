N=int(input())
answer=[]
for i in range(N):
    a,b=map(int,input().split(' '))
    answer.append(a+b)
for j in range(len(answer)):
    print(answer[j])
    