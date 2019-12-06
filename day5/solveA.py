class Foo:
    def __init__(self, comp):
        self.comp = comp
        self.memory = comp.memory
        self.mr = self.memoryReader
        self.mw = self.memoryWriter
        self.hmp()

    def __call__(self, parms, modes):
        if modes == False:
            self.modes = ('0',) * self.hmp()
        else:
            self.modes = ('0',)*(self.hmp()-len(modes))+tuple(modes)
        self.params = parms
        self.main()

    def main(self):
        pass

    def memoryReader(self, num):
        params = self.params
        modes = self.modes
        if modes[-num] == '0':

            return int(self.memory[int(params[num-1])])
        elif modes[-num] == '1':
            #print(num)
            return int(params[num-1])

    def memoryWriter(self, num, val):
        params = self.params
        num -= 1
        self.memory[int(params[num])] = str(val)

    def changePointer(self, num):
        self.comp.pointer = num

class Foo1(Foo):
    def hmp(self):
        return 3

    def main(self):
        ans = self.mr(1) + self.mr(2)
        self.mw(3, ans)

class Foo2(Foo):
    def hmp(self):
        return 3

    def main(self):
        ans = self.mr(1) * self.mr(2)
        self.mw(3, ans)

class Foo3(Foo):
    def hmp(self):
        return 1

    def main(self):
        inp = input()
        self.mw(1, inp)

class Foo4(Foo):
    def hmp(self):
        return 1

    def main(self):
        out = self.mr(1)
        print(out)

class Foo5(Foo):
    def hmp(self):
        return 2

    def main(self):
        if self.mr(1) != 0:
            self.changePointer(self.mr(2))

class Foo6(Foo):
    def hmp(self):
        return 2

    def main(self):
        if self.mr(1) == 0:
            #print(self.mr(2))
            self.changePointer(self.mr(2))

class Foo7(Foo):
    def hmp(self):
        return 3

    def main(self):
        if self.mr(1) < self.mr(2):
            self.mw(3, 1)
        else:
            self.mw(3, 0)

class Foo8(Foo):
    def hmp(self):
        return 3

    def main(self):
        if self.mr(1) == self.mr(2):
            self.mw(3, 1)
        else:
            self.mw(3, 0)

class Computer:
    def __init__(self, inp):
        self.memory = inp
        self.foos = {1:Foo1(self), 2:Foo2(self), 3:Foo3(self), 4:Foo4(self),
        5:Foo5(self), 6:Foo6(self), 7:Foo7(self), 8:Foo8(self), 99:False}
        self.run()

    def readIns(self, ins):
        if len(ins)<=2:
            foo = self.foos[int(ins)]
            return (foo, False)
        else:
            opCode = ins[-2:]
            foo = self.foos[int(opCode)]
            modes = ins[:-2]
            return (foo, modes)

    def doFunc(self, foo, params, modes):
        #print(foo)
        foo(params, modes)

    def run(self):
        self.pointer = 0
        next = True
        while next:
            foo, modes = self.readIns(self.memory[self.pointer])
            if foo == False:
                return 0
            hmp = foo.hmp()
            self.pointer += 1
            params = self.memory[self.pointer:self.pointer+hmp]
            #print(pointer,params)
            self.pointer += hmp
            self.doFunc(foo, params, modes)







with open('input.txt', 'r') as f:
    inp = f.readline().split(',')
com = Computer(inp)
