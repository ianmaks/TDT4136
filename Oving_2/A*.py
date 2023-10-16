import numpy as np
from Map import Map_Obj
import heapq as hq
import random

class Node:

    def __init__(self, position, g, h, parent=None):
        self.parent = parent 
        self.position = position # [x, y]

        self.g = g # distance to start node
        self.h = h # distance to goal node

    def __eq__(self, other):
        return self.position == other.position

    def get_f(self):
        return self.g + self.h
    
    # Updates the distance to start node and parent if a new shorter path has been found
    def update_g(self, new_parent, new_g):
        if (new_g < self.g):
            self.g = new_g
            self.parent = new_parent

    # Get positions of all neighboring nodes
    def get_neighbours_pos(self):
        delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        neighbors = []
        for d in delta:
            neighbors.append((np.array(self.position) - np.array(d)).tolist())
        return neighbors
        
    # Returns true if this node is considered less than the other node. 
    # Used to pop the minimal node from the heap
    def __lt__(self, other):
        if self.get_f() == other.get_f():
            if self.h == other.h:
                return random.choice([True, False])
            else:
                return self.h < other.h
        else:
            return self.get_f() < other.get_f()


# Calculate distance from pos1 to pos2 with the manhattan-method
def manhattan_method(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

# Trace and record optimal path after it is found
def find_path(finish_node, start_node):
    arr = []
    node = finish_node
    while node != start_node:
        arr.append(node.position)
        node = node.parent
    return arr



def __main__():
    task = Map_Obj(4)
    int_map, str_map = task.get_maps()
    
    open = []
    closed = []

    h = manhattan_method(task.get_start_pos(), task.get_goal_pos())
    start_node = Node(task.get_start_pos(), 0, h, None)

    #Push start node to the open list 
    hq.heappush(open, start_node)

    while(True):
        # Select the node with the lowest cost from open, and move it to closed
        current = hq.heappop(open)
        # Add current node to visited nodes
        closed.append(current)

        
        # Break if we have reached the goal
        if current.position == task.get_goal_pos():
            break

        # Get neighbouring positions
        neighbours = current.get_neighbours_pos()
        
        for n in neighbours:
            # Check distance of neighbor to goal
            h = manhattan_method(n, task.get_goal_pos())
            # Create a new node
            new_node = Node(n, current.g + task.get_cell_value(n), h, current)
            # Don't do anything with the node if it's a wall or has been visited before
            if task.get_cell_value(n) == -1 or new_node in closed:
                continue
            # If it's the first time we're discovering this node
            if new_node not in open:
                # Add to heap 
                hq.heappush(open, new_node)
            # Update the neighbor node if necessary
            else:
                for open_node in open:
                    if(open_node == new_node):
                        # Update g-value of neighbor if lower through current node
                        open_node.update_g(new_node.parent, new_node.g)
                        hq.heapify(open)
                        break
            
    nodes_in_path = find_path(current, start_node)
    for node in nodes_in_path:
        str_map[node[0]][node[1]] = ";"
    task.show_map(str_map)



__main__()
