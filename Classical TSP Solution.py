from itertools import permutations


# Graph representation using an adjacency matrix
graph = [
    [0,12,10, 0, 0, 0, 12],  # City 1 (Start)
    [12,0, 8, 12, 0, 0, 0],   # City 2
    [10, 8, 0, 11,3, 0, 9],   # City 3
    [0, 12,11,0, 11,10, 0], # City 4
    [0, 0, 3, 11, 0, 6, 7],    # City 5
    [0, 0, 0, 10, 6, 0, 9],    # City 6
    [12, 0, 9, 0, 7, 9, 0]     # City 7
]

def tsp_brute_force(graph):
    n = len(graph)
    cities = list(range(1, n))  # Exclude starting city (0)
    min_cost = float('inf')  # Start with an infinitely large cost
    best_path = []   # Variable to store the best route

    # Try all possible city orders
    for perm in permutations(cities):
        path = [0] + list(perm) + [0]  # Start and end at city 0
        cost = sum(graph[path[i]][path[i+1]] for i in range(n)) #example path = [0, 2, 3, 1, 0]
        """"
        for cities = [1, 2, 3]:
        Example perutations
        (1, 2, 3)
        (1, 3, 2)
        (2, 1, 3)
        (2, 3, 1)
        (3, 1, 2)
        (3, 2, 1)
        There are (n-1)! permutations to check.  """
    if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Run the TSP brute-force solution
route, cost = tsp_brute_force(graph)
print("Best Route:", route)
print("Minimum Cost:", cost)


#Best Route: [0, 6, 5, 4, 3, 2, 1, 0]
#Minimum Cost: 69