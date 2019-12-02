def brutforce():
    with open('input.txt','r') as f:
        input = f.readline()
        input = input.split(',')
    for a in range(0,100):
        for b in range(0,100):
            try:
                ans = interpreter(a,b,input.copy())
                if ans == 19690720:
                    return(100*a+b)
            except Exception as e:
                pass
def interpreter(noun, verb, input):
    input[1]=str(noun)
    input[2]=str(verb)
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
    return(input[0])
print(brutforce())
