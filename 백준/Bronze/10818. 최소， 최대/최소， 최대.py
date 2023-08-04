N=int(input())
tmp=input().split(' ')
numbers = list(map(int, tmp))
print(f'{min(numbers)} {max(numbers)}')