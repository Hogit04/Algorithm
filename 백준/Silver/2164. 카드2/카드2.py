N = int(input())
# que=[]
# for i in range(N,0,-1):#큐를 만들어주기
#     que.append(i)

# while len(que) != 1:
#     que.pop()# 첫번쨰 버리기
#     tmp=que.pop() #두번째 카드 뽑아서 tmp에 저장
#     que.insert(0,tmp)#제일 왼쪽(뒤)로 보내주기
    
# print(que[0]) # 시간초과 코드

from collections import deque
que=[]
for i in range(1,N+1):
    que.append(i)
deque=deque(que)#덱으로 만들기

while len(deque) != 1:
    deque.popleft()#첫번쨰 버리기
    deque.append(deque.popleft())#첫번째를 맨뒤로
print(deque[0])
    