def check(num):
    num = str(num)
    increasing = list(num) == sorted(num)
    hasPair = any(a==2 for a in map(num.count, num))
    return increasing and hasPair
print(sum(check(num) for num in range(146810, 612564)))
