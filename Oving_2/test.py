from Map import Map_Obj
import numpy as np
import heapq as hq
import random

a = Map_Obj(3)

intmap, stringmap = a.get_maps()

class Node:
    def __init__(self, position, g, h, parent=None):
        self.parent = parent 
        self.position = position # [x, y]
        self.g = g # distance to start node
        self.h = h # distance to goal node

    def get_f(self):
        return self.g + self.h

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        if( self.get_f() == other.get_f()):
            if self.h == other.h:
                return random.choice([True, False])
                
            else:
                return self.h < other.h
        else:
            return self.get_f() < other.get_f()
    
# NODE = Node([1,1], 10, 1)
node1 = Node([1,1], 12, 4)
node2 = Node([2,2], 12, 4)

listOfNodes = []
hq.heappush(listOfNodes, node1)

hq.heappush(listOfNodes, node2)
print([x.get_f() for x in listOfNodes])
print([x.h for x in listOfNodes])
print([x.position for x in listOfNodes])
print(a.get_start_pos())
print(stringmap)
