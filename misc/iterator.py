def factor(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

for i in factor(100):
    print(i)

a = [i for i in factor(100)]
print(a)
