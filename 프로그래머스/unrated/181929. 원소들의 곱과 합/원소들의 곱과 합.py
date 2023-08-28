from math import prod
def solution(num_list):
    pd=prod(num_list)
    sum_num=sum(num_list)
    return 1 if pd<sum_num**2 else 0