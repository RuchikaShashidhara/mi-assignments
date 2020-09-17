import queue

def A_star_Traversal( ):

    # Parameters
    A_star_path = []

    return A_star_path

def UCS_Traversal( ):

    # Parameters
    UCS_path = []

    return UCS_path

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
    t2 = UCS_Traversal( )
    t3 = A_star_Traversal( )

    l.append(t1)
    l.append(t2)
    l.append(t3)

    return l
