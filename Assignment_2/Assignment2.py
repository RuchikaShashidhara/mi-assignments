import queue
import copy

def A_star_Traversal(cost, heuristic, start_point, goals):

    n = len(cost)                                               # Number of Nodes in Graph
    visited = [0 for i in range(n)]                             # Visited Set (0 - not visited, 1 - visited)
    frontier_priority_queue = queue.PriorityQueue(maxsize = n)  # Frontier Priority Queue

    # Insert (estimated_total_cost, (start_point, A*_path_till_start_node, 0)) into priority queue
    frontier_priority_queue.put((heuristic[start_point], (start_point, [start_point], 0)))

    # Until priority queue is not empty
    while(frontier_priority_queue.qsize() != 0):

        # Pop the node information from the priority queue
        total_estimated_cost, nodes_tuple = frontier_priority_queue.get()
        node = nodes_tuple[0]
        A_star_path_till_node = nodes_tuple[1]
        node_cost = nodes_tuple[2]

        # If the node was not visited
        if visited[node] == 0:
            visited[node] = 1

            # If node is a goal_point, return the A* Path till Goal Node
            if node in goals:
                return A_star_path_till_node

            # For every neighbour connected node
            for neighbour_node in range(1, n):
                # If the node is connected and not visited, add it to the priority queue
                if cost[node][neighbour_node] > 0 and visited[neighbour_node] == 0:

                    # Compute total cost till neighbour node
                    total_cost_till_node = node_cost + cost[node][neighbour_node]
                    # Compute estimated total cost for the path
                    estimated_total_cost = total_cost_till_node + heuristic[neighbour_node]

                    # Add the neighbour node to the new A* path list
                    A_star_path_till_neighbour_node = copy.deepcopy(A_star_path_till_node)
                    A_star_path_till_neighbour_node.append(neighbour_node)
                    # Insert (estimated total, (neighbour_node, A_star_path_till_neighbour_node, total cost till neighbour nodes)) into priority queue
                    frontier_priority_queue.put((estimated_total_cost, (neighbour_node, A_star_path_till_neighbour_node, total_cost_till_node)))


def UCS_Traversal(cost, start_point, goals):

    # Parameters
    #UCS_path = []                                               # UCS Traversal Path
    # I have just appeneded a list of node paths corresponding to path cost till that node into the PQ itself
    # its better if we make a backtracking path tree DS ourselves
    n = len(cost)                                               # Number of Nodes in Graph
    visited = [0 for i in range(n)]                             # Visited Set (0 - not visited, 1 - visited)
    frontier_priority_queue = queue.PriorityQueue(maxsize = n)  # Frontier Priority Queue

    # Insert (0, (start_point, UCS_path_till_start_point)) into priority queue
    frontier_priority_queue.put((0, (start_point, [start_point])))

    # Until priority queue is not empty
    while(frontier_priority_queue.qsize() != 0):

        # Pop the node information from the priority queue
        node_cost, nodes_tuple = frontier_priority_queue.get()
        node = nodes_tuple[0]
        ucs_path_till_node = nodes_tuple[1]
        #print(ucs_path_till_node)

        # If the node was not visited
        if visited[node] == 0:
            visited[node] = 1

            # If node is a goal_point, return the UCS Path till Goal Node
            if node in goals:
                return ucs_path_till_node

            # For every neighbour connected node
            for neighbour_node in range(1, n):
                # Connected node has cost > 0
                if cost[node][neighbour_node] > 0:
                    # If the connected node is not visited, insert it into the priority queue
                    if visited[neighbour_node] == 0:
                        # Add the total cost till node
                        total_cost_till_node = node_cost + cost[node][neighbour_node]
                        # Add the neighbour node to the new ucs path list
                        ucs_path_till_neighbour_node = copy.deepcopy(ucs_path_till_node)
                        ucs_path_till_neighbour_node.append(neighbour_node)
                        # Insert (total cost till node, (neighbour_node, UCS_path_till_neighbour_node)) into priority queue
                        frontier_priority_queue.put((total_cost_till_node, (neighbour_node, ucs_path_till_neighbour_node)))


def DFS_Traversal(cost, start_point, goals):

    # Parameters
    DFS_path = []                                  # DFS Traversal Path
    n = len(cost)                                  # Number of Nodes in Graph
    visited = [0 for i in range(n)]                # Visited Set (0 - not visited, 1 - visited)
    frontier_stack = queue.LifoQueue(maxsize = n)  # Frontier Stack

    # Insert start_point into stack
    frontier_stack.put(start_point)

    # Until stack is not empty
    while(frontier_stack.qsize() != 0):

        # Pop the node from the stack and append it to the DFS Traversal Path
        node = frontier_stack.get()
        DFS_path.append(node)

        # If the node was not visited
        if visited[node] == 0:
            visited[node] = 1

            # If node is a goal_point, return the DFS Traversal Path
            if node in goals:
                return DFS_path

            # For every neighbour connected node
            # (taken from n-1 to 1, to get first lexicological path)
            for neighbour_node in range(n-1, 0, -1):
                # Connected node has cost > 0
                if cost[node][neighbour_node] > 0:
                    # If the connected node is not visited, insert it into the stack
                    if visited[neighbour_node] == 0:
                        frontier_stack.put(neighbour_node)


# Let's remove this definition comment later on
'''
Function tri_traversal - performs DFS, UCS and A* traversals and
returns the path for each of these traversals

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the
starting index is from 1 and not 0.
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1'
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n], start_point, goals[m]

NOTE : you are allowed to write other helper functions that you
can call in the given fucntion
'''

def tri_traversal(cost, heuristic, start_point, goals):

    l = []

    t1 = DFS_Traversal(cost, start_point, goals)
    t2 = UCS_Traversal(cost, start_point, goals)
    t3 = A_star_Traversal(cost, heuristic, start_point, goals)

    l.append(t1)
    l.append(t2)
    l.append(t3)

    return l
