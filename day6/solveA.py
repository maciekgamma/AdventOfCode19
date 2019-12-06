class Planet:
    def __init__(self):
        self.orbs = []

    def count_orbs(self):
        all = 1
        for p in self.orbs:
            all += p.count_orbs()
        return all

with open('input.txt', 'r') as f:
    all = f.readlines()
planets = {}
for l in all:
    i, o = l[:-1].split(')')
    if i not in planets:
        planets[i] = Planet()
    if o not in planets:
        planets[o] = Planet()
    planets[i].orbs.append(planets[o])
    
all=sum(p.count_orbs() for p in planets.values())-len(planets)
print(all)
