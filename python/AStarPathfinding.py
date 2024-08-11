# Description: A* Pathfinding Algorithm
import heapq
import random

class Node:
    def __init__(self, x, y, val, parent=None, neighbors=None) -> None:
        self.x = x
        self.y = y
        self.parent = parent
        self.neighbors = neighbors
        self.g = 0
        self.h = 0
        self.f = 0

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.f})"
    
class NodeList:
    def __init__(self, w, h) -> None:
        self.nodes = []
        self.width = w
        self.height = h
    
    def add(self, node: Node):
        self.nodes.append(node)
        
    def remove(self, node: Node):
        self.nodes.remove(node)
        
    def generateList(self, node: Node):
        for x in range(self.width):
            for y in range(self.height):
                node = random.randint(0, 100)
                self.add(Node(x, y, node))
        
    

class Solution:
    def AStar(self, NodeList) -> NodeList:
        openList = []
        closedList = []
        pass
    


A = Solution()
