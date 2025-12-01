def f(n):
    if n<=1:
        return 0.5
    else:
        return (n+1)*f(n-1)

#print(f(200)/f(198))   #nan

a = [0]*202
a[0] = 0.5
a[1] = 0.5
for i in range(2, len(a)):
    a[i] = (i+1)*a[i-1]
    print(a[i], '-значение  ', i, '-номер')

print(a[200]/a[198])

-возвращает nan & inf 
