sum=0
with open('input.txt') as f:
    for mass in f.readlines():
        while(int(int(mass)/3)-2>0):
            mass=int(int(mass)/3)-2
            sum+=mass
print(sum)
