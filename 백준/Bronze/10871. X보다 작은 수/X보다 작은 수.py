N,X=map(int,input().split(' '))
tmp=input().split(' ')

answer=''
for i in range(len(tmp)):
    if int(tmp[i])<X:
        answer+=f'{tmp[i]} '
print(answer[:-1])