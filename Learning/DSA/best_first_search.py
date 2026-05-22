from queue import PriorityQueue

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 10,
    'B': 5,
    'C': 7,
    'D': 2,
    'E': 1,
    'F': 6,
    'G': 0
}

def best_first_search(start, goal):
    visited = []
    
    pq = PriorityQueue()
    
    # Put start node with heuristic
    pq.put((heuristic[start], start))

    while not pq.empty():

        h, node = pq.get()

        if node not in visited:

            print(node, end=" ")
            visited.append(node)

            # Goal found
            if node == goal:
                print("\nGoal Reached!")
                return

            # Add neighbors
            for neighbor in graph[node]:
                pq.put((heuristic[neighbor], neighbor))

# Run
best_first_search('A', 'G')