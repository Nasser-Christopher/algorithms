# Description: A* Pathfinding Algorithm
import heapq
import random

# imported libraries (Dependencies)
import numpy as np
import matplotlib.pyplot as plt


class Node:
    def __init__(self, x, y, val=0, parent=None, neighbors=None) -> None:
        self.x = x
        self.y = y
        self.parent = parent
        self.neighbors = neighbors
        self.value = val
        self.g = 0
        self.h = 0
        self.f = self.value

    def calculate_h(self, end):
        self.h = abs(self.x - end.x) + abs(self.y - end.y)
        self.f += self.h
        
    def calculate_g(self, start):
        self.g = abs(self.x - start.x) + abs(self.y - start.y)
        self.f += self.g

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
        
    def generateList(self):
        for x in range(self.width):
            for y in range(self.height):
                nodeValue = random.randint(0, 100)
                self.add(Node(x, y, nodeValue))
        self.set_neighbors()
                
    def getNode(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None
    
    def set_neighbors(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for node in self.nodes:
            node.neighbors = []
            for dx, dy in directions:
                neighbor_x = node.x + dx
                neighbor_y = node.y + dy
                if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                    neighbor = self.getNode(neighbor_x, neighbor_y)
                    if neighbor is not None:
                        node.neighbors.append(neighbor)
    
    
class Solution:
    def __init__(self) -> None:
        self.NodeList = NodeList(10, 10)
        self.NodeList.generateList()
        self.AStar(self.NodeList)
        
    def AStar(self, nodeList:NodeList, startingNode:Node, endingNode:Node) -> NodeList:
        openList = []
        closedList = []
        pass
    


A = Solution()
