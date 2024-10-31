n=int(input())
output=0
for _ in range(n):
   P, T, V=map(int, input().split())
   if P+T+V > 1:
      output+=1
print(output)
   