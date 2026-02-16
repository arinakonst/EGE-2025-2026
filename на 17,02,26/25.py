def f(n):      #поиск простых делителей
   i = 2
   dels = []
   while i * i <= n:
       while n % i == 0:
           dels.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       dels.append(n)
   return list(set(list(map(int, dels))))

cou = 0
n = 5200001
while n >= 5200000:
    res = f(n)
    if len(res) != 0 and res[0] != n:    №проверка, чтобы в простых делителях не лежало само число
        m = min(res) + max(res)
    else: m = 0
    if m > 50_000 and m%100 == 26:
        print(n, m)
        cou += 1
    n += 1
    if cou == 5: break

5200105 1040026
5200369 226126
5200869 1733626
5201169 1733726
5201365 80026
