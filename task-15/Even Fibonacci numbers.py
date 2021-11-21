def even_fibonacci_sum(n):
    ef_2 = 1 #Ef-2
    ef_1 = 1 #Ef-1
    sum = 0
    while True :
        ef = ef_2 + ef_1 #Ef
        if ef >= n: return sum
        if ef % 2 == 0: sum += ef
        ef_2, ef_1 = ef_1, ef

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(even_fibonacci_sum(n))
