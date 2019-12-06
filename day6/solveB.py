class Planet:
    def __init__(self):
        self.orbs = []

    def count_orbs(self):
        all = 1
        for p in self.orbs:
            all += p.count_orbs()
        return all

    def hasPlanet(self, planet):
        if planet in self.orbs:
            return True
        elif len(self.orbs)>0:
            return any(p.hasPlanet(planet) for p in self.orbs)
        return False

    def distanceToPlanet(self, planet):
        if planet in self.orbs:
            return 0
        for p in self.orbs:
            if p.hasPlanet(planet):
                return 1+p.distanceToPlanet(planet)

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
common = []
for p in planets.values():
    if p.hasPlanet(planets['SAN']) and p.hasPlanet(planets['YOU']):
        common.append(p)
minD, np = min((p.count_orbs(),p) for p in common)
disY = np.distanceToPlanet(planets['YOU'])
disS = np.distanceToPlanet(planets['SAN'])
print(disY+disS)
