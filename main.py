import sys
import math


def calc_distance(ship1, ship2):
    # print(str(ship1) + " " + str(ship2),file=sys.stderr)
    a = ship1.x - ship2.x
    b = ship1.y - ship2.y
    dist = math.sqrt(a * a + b * b)

    return dist


class Unit:
    list_of_unit = []

    def __init__(self):
        self.x = 0
        self.y = 0
        self.owner = 0
        self.unit_type = 0
        self.health = 0


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Site:
    list_of_site = {}
    lisf_of_distance = {}

    def __init__(self):
        self.id = 0
        self.owner = 0
        self.structure_type = 0
        self.type_army = -1
        self.turn_remaining = 0
        self.type_building = 0
        self.x = 0
        self.y = 0
        self.max_mine_size = 0
        self.gold = 0
        self.radius = 0
        self.rank = 0
        self.portee = 0
        self.distance = 0

    @staticmethod
    def calcDistanceSite():
        Site.lisf_of_distance={}
        for i in Site.list_of_site:
            if Site.list_of_site[i].owner == -1:
                dist = calc_distance(Site.list_of_site[i],Queen.list_of_queen[0])
                Site.lisf_of_distance[dist] = Site.list_of_site[i];
            
    @staticmethod
    def findBestMineSite():
        Site.calcDistanceSite()
        dists = list(Site.lisf_of_distance.keys())
        print(dists,file=sys.stderr)
        dists.sort(reverse=True)
        for d in dists:
            print(" dd  " + str(Site.lisf_of_distance[d].max_mine_size) + "//" + str(d),file=sys.stderr)
            if Site.lisf_of_distance[d].max_mine_size >= 3:
                return Site.lisf_of_distance[d]
                
        return None
            
        

    @staticmethod
    def found_nearest_free_site(queen):
        distance = -1
        site = None
        for i in Site.list_of_site:
            if Site.list_of_site[i].owner == -1:  # or (Site.list_of_site[i].structure_type == 0 and Site.list_of_site[i].rank<2):
                #if (queen.left and Site.list_of_site[i].x < 1200) or (not queen.left and Site.list_of_site[i].x > 800): 
                d = calc_distance(queen, Site.list_of_site[i])
                if distance == -1 or distance > d:
                    distance = d
                    site = Site.list_of_site[i]
        """
        if site is None:
            for i in Site.list_of_site:
                if Site.list_of_site[i].owner == 1:
                    d = calc_distance(queen, Site.list_of_site[i])
                    if distance == -1 or distance > d:
                        distance = d
                        site = Site.list_of_site[i]
        """
        return site

    @staticmethod
    def found_nearest_site_from_queen(_type, queen):
        distance = -1
        site = None
        for i in Site.list_of_site:
            if Site.list_of_site[i].owner == 0 and Site.list_of_site[i].structure_type == _type:
                d = calc_distance(queen, Site.list_of_site[i])
                if distance == -1 or distance > d:
                    distance = d
                    site = Site.list_of_site[i]
        return site

    @staticmethod
    def get_number_buildings_per_type(_type,_owner=0):
        nb = 0
        for i in Site.list_of_site:
            if Site.list_of_site[i].owner == _owner and Site.list_of_site[i].structure_type == _type:
                nb += 1
        return nb
    
    @staticmethod
    def has_giant_barracks():
        for i in Site.list_of_site:
            if Site.list_of_site[i].owner == 0 and Site.list_of_site[i].structure_type == 2 and Site.list_of_site[i].type_army == 2:
                return Site.list_of_site[i]
        return None
                


class Queen:
    list_of_queen = {}

    def __init__(self):
        self.health = 0
        self.gold = 0
        self.x = -1
        self.y = -1
        self.left = False


Queen.list_of_queen[0] = Queen()
Queen.list_of_queen[1] = Queen()


class GameState:
    instance = None

    def __init__(self):
        GameState.instance = self
        self.target = None
        self.action = 0  # build Mine
        self.giant = False

    def take_decision(self):
        nb_barracks = Site.get_number_buildings_per_type(2)
        nb_tower = Site.get_number_buildings_per_type(1)
        nb_tower_ennemy = Site.get_number_buildings_per_type(1,1)
        nb_mine = Site.get_number_buildings_per_type(0)
        distance = -1
        for u in Unit.list_of_unit:
            if u.owner == 1:
                dist = calc_distance(Queen.list_of_queen[0], u)
                if distance == -1 or distance > dist:
                    distance = dist
                    if distance < 80:
                        break

        #print("nb_tower_ennemy" + str(nb_tower_ennemy) + "//" + str( 
        #if nb_tower == 4 and self.target is None:
        #    self.action = 4
        #    return self.move_to_tower()
        if nb_tower_ennemy > 3 and  Site.has_giant_barracks() is None:
            self.action = 3
            return self.build_giant()
        elif distance < 100 and distance != -1 and nb_tower < 4:
            self.action = 1
            return self.build_tower()
        elif self.target is None:
            
            if nb_mine>4 and nb_barracks<2:
                self.action = 2
                return self.build_barracks()
            if nb_mine < 2:
                self.action = 0
                return self.build_mine()
            elif nb_tower < 1:
                self.action = 1
                return self.build_tower()
            elif nb_barracks < 1:
                self.action = 2
                return self.build_barracks()
            elif nb_tower == nb_barracks:
                self.action = 1
                return self.build_tower()
            elif nb_mine == nb_barracks:
                self.action = 0
                return self.build_mine()
            elif nb_mine <= nb_tower:
                print("HERE 5",file=sys.stderr)
                self.action = 0
                return self.build_mine()
            elif nb_tower < nb_mine:
                self.action = 1
                return self.build_tower()
            else:
                print("HERE ",file=sys.stderr)
                print("WAIT")
                return true

        else:
            #if self.target.owner == -1:
            if self.action == 0:
                return self.build_mine()
            elif self.action == 1:
                return self.build_tower()
            elif self.action == 2:
                return self.build_barracks()
            elif self.action == 3:
                return self.build_giant()
            elif self.action == 4:
                return self.move_to_tower()
            else:
                print("HERE 2",file=sys.stderr)
                print("WAIT")
                return False
                #else:
                 #   self.target = None
                 #   return False
        print("HERE 3",file=sys.stderr)
        print("WAIT")
        return True

    def run(self):
        action_done = False
        i = 0
        while not action_done and i < 5:
            action_done = self.take_decision()
            i+=1
            
        if not action_done:
            print("HERE 4",file=sys.stderr)
            print("WAIT")
            
        self.train()
    
    def move_to_tower(self):
        if self.target is None:
            self.target = Site.found_nearest_site_from_queen(0,Queen.list_of_queen[0])
        print("MOVE " + str(self.target.x) + " " + str(self.target.y))
        return True
    
    def train(self):
        print ("TOOT " + str(Site.has_giant_barracks()) + "//" + str(self.giant),file=sys.stderr)
        if Site.has_giant_barracks() is not None and self.giant == False:
            if Queen.list_of_queen[0].gold >= 140:
                print("TRAIN " + str(Site.has_giant_barracks().id))
                self.giant = True
            else:
                print("TRAIN")
        else:
            barracks = ""
            nbBarracks = Queen.list_of_queen[0].gold // 80
            for i in Site.list_of_site:
                if nbBarracks <= 0:
                    break
                if Site.list_of_site[i].owner == 0 and Site.list_of_site[i].turn_remaining == 0 and Site.list_of_site[i].type_army == 0:
                    barracks += " " + str(i)
                    nbBarracks -= 1
            print("TRAIN" + barracks)
    # First line: A valid queen action
    # Second line: A set of training instructions

        
        
    def build_giant(self):
        if self.target is None:
            self.target = Site.found_nearest_free_site(Queen.list_of_queen[0])
        if self.target.owner == -1:
            print("BUILD " + str(self.target.id) + " BARRACKS-GIANT")
        else:
            self.target = None
            return False
        return True    

    def build_barracks(self):
        if self.target is None:
            self.target = Site.found_nearest_free_site(Queen.list_of_queen[0])
        if self.target.owner == -1:
            print("BUILD " + str(self.target.id) + " BARRACKS-KNIGHT")
        else:
            self.target = None
            return False
        return True

    def build_tower(self):
        if self.target is None:
            self.target = Site.found_nearest_free_site(Queen.list_of_queen[0])
        if self.target.owner == -1:
            print("BUILD " + str(self.target.id) + " TOWER")
        elif self.target.owner==0 and self.target.portee < 500:
            print("BUILD " + str(self.target.id) + " TOWER")
        else:
            self.target = None
            return False
        return True

    def build_mine(self):
        print("HERE 11",file=sys.stderr)
        if self.target is None:
            print("HERE 12" + str(self.action),file=sys.stderr)
            #self.target = Site.findBestMineSite()
            #if self.target is None:
            self.target = Site.found_nearest_free_site(Queen.list_of_queen[0])
            print("HERE 122" + str(self.target),file=sys.stderr)
        #elif self.target.owner == -1 and self.target.max_mine_size !=-1 and self.target.max_mine_size <3:
        #    self.action = 1
        #    return False
        if self.target.owner == -1:
            print("BUILD " + str(self.target.id) + " MINE")
            
        elif self.target.owner == 0:
            print("HERE 10",file=sys.stderr)
            if self.target.rank < self.target.max_mine_size and self.target.rank < 4:
                print("BUILD " + str(self.target.id) + " MINE")
            else:
                print("HERE 13",file=sys.stderr)
                self.target = None
                return False
        else:
            self.target = None
            return False
        return True


GameState()

num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    if site_id not in Site.list_of_site:
        temp = Site()
        temp.id = site_id
        temp.x = x
        temp.y = y
        temp.radius = radius
        Site.list_of_site[site_id] = temp

# game loop
while True:
    
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    Queen.list_of_queen[0].gold = gold
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, gold, max_mine_size, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]

        temp = Site.list_of_site[site_id]
        temp.structure_type = structure_type
        temp.owner = owner
        if structure_type == 0:
            temp.rank = param_1
        else:
            temp.turn_remaining = param_1
        if structure_type == 1:
            temp.portee = param_2
        temp.type_army = param_2
        temp.max_mine_size = max_mine_size
        
        temp.gold = gold
    Site.calcDistanceSite()
    num_units = int(input())
    Unit.list_of_unit = []
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        if unit_type == -1:
            if Queen.list_of_queen[owner].x == -1:
                if x < 1000:
                    Queen.list_of_queen[owner].left = True
                else:
                    Queen.list_of_queen[owner].left = False
            Queen.list_of_queen[owner].x = x
            Queen.list_of_queen[owner].y = y
            Queen.list_of_queen[owner].health = health

        else:
            temp = Unit()
            temp.x = x
            temp.y = y
            temp.owner = owner
            temp.unit_type = unit_type
            temp.health = health
            Unit.list_of_unit.append(temp)

    GameState.instance.run()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
