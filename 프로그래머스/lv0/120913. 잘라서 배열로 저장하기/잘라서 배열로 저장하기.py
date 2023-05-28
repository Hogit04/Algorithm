def solution(my_str, n):
    tmp=''
    count=0
    answer=[]
    for i in range(len(my_str)):
        tmp+=my_str[i]
        count+=1
        if count%n==0:
            count=0
            answer.append(tmp)
            tmp=''
    if len(tmp)!=0:
        answer.append(tmp)
    return answer