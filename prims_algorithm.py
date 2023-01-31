mst = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

adjacencyList = [[0, 4, 4, 0, 0, 0], [4, 0, 2, 0, 0, 0], [4, 2, 0, 3, 2, 4],
[0, 0, 3, 0, 0, 3], [0, 0, 3, 0, 0, 3], [0, 0, 4, 3, 3, 0]]

unvisitedNodes = [1, 2, 3, 4, 5]

currentNodes = [0]

while len(unvisitedNodes) > 0:
    smallestDistance = ""
    nearestNode = ""
    currentNode = 0
    for node in currentNodes :
        adjacentNode = 0
        for value in adjacencyList[node]:
            if value > 0:
                if adjacentNode in unvisitedNodes:
                    if smallestDistance == "":
                        smallestDistance = value
                        nearestNode = adjacentNode
                        currentNode = node
                    if value < smallestDistance:
                        smallestDistance = value
                        nearestNode = adjacentNode
                        currentNode = node
            adjacentNode = adjacentNode + 1

    unvisitedNodes.remove(nearestNode)
    currentNodes.append(nearestNode)

    mst[nearestNode][node] = smallestDistance
    mst[node][nearestNode] = smallestDistance

print(mst)