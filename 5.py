def f(n):
    nums = [int(num) for num in str(n)]
    s = sum(nums)
    m = max(nums) + min(nums)
    l = nums[0]
    r = n%10
    p1 = s-l
    p2 = m-r
    if p1 <= p2:
        return str(p1) + str(p2)
    return str(p2) + str(p1)

a = []
for n in range(100000, 1000000):
    z = f(n)
    if z == '222':
        a.append(n)

print(max(a))   #996007
