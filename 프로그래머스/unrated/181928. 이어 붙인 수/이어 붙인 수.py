def solution(num_list):
    even=[]
    odd=[]
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            even.append(str(num_list[i]))
        else:
            odd.append(str(num_list[i]))
    odd_num=''.join(odd)
    even_num=''.join(even)
    return int(odd_num)+int(even_num)