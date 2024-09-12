# Description: A* Pathfinding Algorithm
import heapq
import random

# imported libraries (Dependencies)
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Node:
    def __init__(self, x, y, value, walkable=True):
        self.x = x
        self.y = y
        self.value = value
        self.walkable = walkable
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')
        self.parent = None
        self.neighbors = []

    def calculate_h(self, endingNode):
        self.h = abs(self.x - endingNode.x) + abs(self.y - endingNode.y)
        self.f = self.g + self.h
        

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
        
    # def set_walkable(self, x, y, walkable):
    #     node = self.getNode(x, y)
    #     if node is not None:
    #         node.walkable = walkable
        
    def generateList(self):
        for x in range(self.width):
            for y in range(self.height):
                nodeValue = 0 ## TODO: Remove the nodeValue from the Node class
                walkable = random.choice([True, False, True])
                self.add(Node(x, y, nodeValue, walkable = walkable))
        # self.set_neighbors()
                
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
                        print(f"Node ({node.x}, {node.y}) added neighbor ({neighbor.x}, {neighbor.y})")
                        

    # def get_neighbors(self, node:Node):
    #     return node.neighbors
    
    
class Solution:
    def AStar(self, nodeList:NodeList, startingNode:Node, endingNode:Node) -> NodeList:
        openList = []
        closedSet = set()
        steps = []  # To store the state at each step (for graphing later)
        
        startingNode.g = 0
        startingNode.calculate_h(endingNode)
        heapq.heappush(openList, startingNode)
        
        while openList:
            current = heapq.heappop(openList)
            closedSet.add(current)
            
            steps.append((list(openList), list(closedSet)))
            
            if current.x == endingNode.x and current.y == endingNode.y:
                endingNode.g = current.g
                endingNode.f = current.f
                return closedSet, steps
            
            for neighbor in current.neighbors:
                if neighbor in closedSet or not neighbor.walkable:
                    continue
                
                tentative_g = current.g + 1
                if tentative_g < neighbor.g or neighbor == endingNode:
                    neighbor.g = tentative_g
                    neighbor.calculate_h(endingNode)
                    neighbor.parent = current
            
                    if neighbor not in openList:
                        heapq.heappush(openList, neighbor)
                        
            # print(f"Processing Node: ({current.x}, {current.y}) || g = {current.g}, h = {current.h}, f = {current.f}")
            # print(f"Open List: {[str(node) for node in openList]}")
            # print(f"Closed Set: {[str(node) for node in closedSet]}")
                        
        if endingNode.f == float('inf'):
            print("No valid path found to the ending node.")
            endingNode.f = -1
                        
        return closedSet, steps
        
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
                    ax.text(node.x, node.y, f'{node.f:.1f}', fontsize=12, ha='center', va='center')
                elif node in openList:
                    ax.scatter(node.x, node.y, color='green', marker='o')
                    ax.text(node.x, node.y, f'{node.f:.1f}', fontsize=12, ha='center', va='center')
                else:
                    ax.scatter(node.x, node.y, color='gray', marker='x')
                    ax.text(node.x, node.y, f'{node.f:.1f}', fontsize=12, ha='center', va='center')
                
                
                    
            for node in closedList:
                if node.parent:
                    x_values = [node.x, node.parent.x]
                    y_values = [node.y, node.parent.y]
                    ax.plot(x_values, y_values, color='orange')

            ax.set_title(f"Step {frame + 1}")
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.grid(True)

        ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False)
        plt.show()
        
        
    





A = Solution()


test_array = NodeList(10, 10)
test_array.generateList()
startingNode =  test_array.getNode(0, 0)
startingNode.walkable = True
endingNode =  test_array.getNode(9, 9)
endingNode.walkable = True
test_array.set_neighbors()

path, steps = A.AStar(test_array, startingNode, endingNode)
print(endingNode)
A.visualize_path(steps, test_array)
