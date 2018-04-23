import sys
import math

def calcDistance(ship1, ship2):
    # print(str(ship1) + " " + str(ship2),file=sys.stderr)
    a = ship1.x - ship2.x
    b = ship1.y - ship2.y
    dist = math.sqrt(a * a + b * b)

    return dist

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Site:
    listOfSite = {}
    def __init__(self):
        self.id = 0
        self.owner = 0
        self.structureType = 0
        self.turnRemaining = 0
        self.typeBuilding = 0
        self.x = 0
        self.y = 0
        self.radius = 0
        
    @staticmethod
    def foundNearestFreeSite(queen):
        distance = -1
        site = None
        for i in Site.listOfSite:
            if Site.listOfSite[i].owner != 0:
                d = calcDistance(queen, Site.listOfSite[i])
                if distance == -1 or distance > d:
                    distance = d
                    site = Site.listOfSite[i]
        return site
        
    @staticmethod
    def foundNearestSiteFromQueen(_type,queen):
        distance = -1
        site = None
        for i in Site.listOfSite:
            if Site.listOfSite[i].owner == 0 and Site.listOfSite[i].structureType == _type:
                d = calcDistance(queen, Site.listOfSite[i])
                if distance == -1 or distance > d:
                    distance = d
                    site = Site.listOfSite[i]
        return site
        
    @staticmethod
    def getNumberBuildingsPerType(_type):
        nb = 0
        for i in Site.listOfSite:
            if Site.listOfSite[i].structureType == _type:
                nb+=1
        return nb
        
class Queen:
    def __init__(self):
        self.health = 0
        self.gold = 0
        self.x = 0
        self.y = 0
        
queen = Queen()
queenEnnemy = Queen()

num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    if site_id not in Site.listOfSite:
        temp = Site()
        temp.id = site_id
        temp.x = x
        temp.y = y
        temp.radius = radius
        Site.listOfSite[site_id] = temp
        
        

# game loop
while True:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    queen.gold = gold
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        
        temp = Site.listOfSite[site_id]
        temp.structureType = structure_type
        temp.owner = owner
        temp.turnRemaining = param_1
        temp.typeBuilding = param_2
        
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        if unit_type == -1 and owner == 0:
            queen.health = health
            queen.x = x
            queen.y = y
        elif unit_type == -1 and owner == 1:
            queenEnnemy.x = x
            queenEnnemy.y = y
            queenEnnemy.health = health

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    barracks = ""
    site = Site.foundNearestFreeSite(queen)        
    if site is not None:
        if Site.getNumberBuildingsPerType(2) <3 :
            print("BUILD " + str(site.id) + " BARRACKS-KNIGHT")
        elif Site.getNumberBuildingsPerType(1) < 3:
            print("BUILD " + str(site.id) + " TOWER")
        else:
            site = Site.foundNearestSiteFromQueen(1,queen)
            print("MOVE " + str(site.x) + " " + str(site.y))
    else:
        print("WAIT")
    
    nbBarracks = queen.gold // 80
    for i in Site.listOfSite:
        if nbBarracks <=0 :
            break
        if Site.listOfSite[i].owner ==0 and Site.listOfSite[i].turnRemaining ==0:
            barracks += " " + str(i)
            nbBarracks -= 1
            

    # First line: A valid queen action
    # Second line: A set of training instructions
    
    print("TRAIN" + barracks)