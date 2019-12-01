sum=0
with open('input.txt') as f:
    for mass in f.readlines():
        sum+=int(int(mass)/3)-2
print(sum)
