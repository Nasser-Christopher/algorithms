# Description: A* Pathfinding Algorithm
import heapq
import random

# imported libraries (Dependencies)
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Node:
    def __init__(self, x, y, val=0, parent=None, neighbors=None, walkable = True) -> None:
        self.x = x
        self.y = y
        self.walkable = walkable
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
        return f"Node:({self.x}, {self.y} || f = {self.f})"
    
class NodeList:
    def __init__(self, w, h) -> None:
        self.nodes = []
        self.width = w
        self.height = h
    
    def add(self, node: Node):
        self.nodes.append(node)
        
    def remove(self, node: Node):
        self.nodes.remove(node)
        
    def set_walkable(self, x, y, walkable):
        node = self.getNode(x, y)
        if node is not None:
            node.walkable = walkable
        
    def generateList(self):
        for x in range(self.width):
            for y in range(self.height):
                nodeValue = random.randint(0, 10)
                walkable = random.choice([True, False, True, True]) 
                self.add(Node(x, y, nodeValue, walkable = walkable))
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
                    if neighbor is not None and neighbor.walkable:
                        node.neighbors.append(neighbor)
                        
    def get_neighbors(self, node:Node):
        return node.neighbors
    
    
class Solution:
    def AStar(self, nodeList:NodeList, startingNode:Node, endingNode:Node) -> NodeList:
        openList = []
        closedList = []
        steps = []  # To store the state at each step
        
        # startingNode.g = 0
        # startingNode.calculate_h(endingNode)
        # startingNode.calculate_g(startingNode)
        
        
        heapq.heappush(openList, startingNode)
        
        for node in nodeList.nodes:
            node.calculate_h(endingNode)
            node.calculate_g(startingNode)
            
        while openList:
            current = heapq.heappop(openList)
            closedList.append(current)
            
            steps.append((list(openList), list(closedList)))
            
            if current == endingNode:
                return closedList, steps
            
            for neighbor in current.neighbors:
                if neighbor in closedList or not neighbor.walkable:
                    continue
                
                
                
                tentative_g = current.g + 1
                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.parent = current
                    neighbor.f = neighbor.g + neighbor.h
            # heapq.heapify(openList)
            
                    if neighbor not in openList:
                            heapq.heappush(openList, neighbor)
        return closedList, steps
                        
            
    def visualize_path(self, steps, nodeList: NodeList):
        fig, ax = plt.subplots(figsize=(10, 10))

        def update(frame):
            ax.clear()
            openList, closedList = steps[frame]

            for node in nodeList.nodes:
                if not node.walkable:
                    ax.scatter(node.x, node.y, color='red', marker='x')
                elif node in closedList:
                    ax.scatter(node.x, node.y, color='blue', marker='o')
                elif node in openList:
                    ax.scatter(node.x, node.y, color='green', marker='o')
                else:
                    ax.scatter(node.x, node.y, color='gray', marker='o')

            ax.set_title(f"Step {frame + 1}")
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.grid(True)

        ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False)
        plt.show()
        
        
    





# TODO: Implement a Matplotlib visualization of the pathfinding algorithm
A = Solution()


test_array = NodeList(10, 10)
test_array.generateList()
startingNode =  test_array.getNode(0, 0)
startingNode.walkable = True
endingNode =  test_array.getNode(9, 9)
endingNode.walkable = True

path, steps = A.AStar(test_array, startingNode, endingNode)
A.visualize_path(steps, test_array)
