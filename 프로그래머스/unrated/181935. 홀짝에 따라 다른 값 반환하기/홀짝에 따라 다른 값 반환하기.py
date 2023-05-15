def solution(n):
    answer=[]
    if n%2==0:
        for i in range(n+1):
            if i%2==0:
                answer.append(i**2)
    else:
        for i in range(n+1):
            if i%2!=0:
                answer.append(i)
    return sum(answer)