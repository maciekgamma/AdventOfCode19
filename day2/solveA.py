with open('input.txt','r') as f:
    input = f.readline()
    input = input.split(',')
input[1]='12'
input[2]='2'
next = True
position = 0
while(next):
    operation = int(input[position])
    if operation==99:
        next = False
    else:
        varA=int(input[int(input[position+1])])
        varB=int(input[int(input[position+2])])
        if operation == 1:
            output = varA+varB
        else:
            output = varA*varB
        output_position = int(input[position+3])
        input[output_position]=output
        position+=4
print(input[0])
