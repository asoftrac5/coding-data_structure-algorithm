class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        # undirected graph
        # for k in self.adjacentList.keys():
        #     if k == node1:
        #         self.adjacentList.get(k).append(node2)
        #     if k == node2:
        #         self.adjacentList.get(k).append(node1)
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

        return self

    def showConnections(self):
        for node in self.adjacentList:
            connections = " ".join(self.adjacentList[node])
            print(f"{node} --> {connections}")

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')

myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()
# Answer:
# 0 --> 1 2
# 1 --> 3 2 0
# 2 --> 4 1 0
# 3 --> 1 4
# 4 --> 3 2 5
# 5 --> 4 6
# 6 --> 5
print(f"Number of Nodes: {myGraph.numberOfNodes}")

# adjacentList = {
#     "0": ["1", "2"],
#     "1": ["3", "2", "0"]
# }
# keys = adjacentList.keys()
# values = adjacentList.values()
# print(adjacentList.get("0"))
# print(keys)
# print(values)
# print("\n")
# print("Show connections")
# for k, v in enumerate(adjacentList.items()):
#     print(f"{k} --> {v}")