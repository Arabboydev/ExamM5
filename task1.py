def fibonachi_sonlar(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 20
for num in fibonachi_sonlar(n):
    print(num)