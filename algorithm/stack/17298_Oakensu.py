#  오~~~큰수
def NGE(n, arr):
    result = [-1]*n
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]<arr[i]:
            result[stack.pop()]=arr[i]
        stack.append(i)
    
    return result

n = int(input())

arr = list(map(int,input().split()))

result = NGE(n,arr)

print(*result)