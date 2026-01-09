for p in range(11, 101):
    for x in range(1, 500001):
        a = 1 + 10*p + 9*p**2 + 2*p**3
        b = 1 + 7*p + 7*p**2 + 7*p**3 + 4*p**4
        c = 10 + 2*p + 1*p**2
        if a + b + c == 1000000 + x:
            print(p)
            break
        
