def sum(n, a):
    d = n // a
    return a * (d * (d+1)) // 2
  
def euler1(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    print(euler1(N - 1)) 
