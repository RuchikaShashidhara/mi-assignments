import queue
import copy

def path_list_append(path_dict, node_cost, path_till_node):
    if(node_cost not in path_dict):
        path_dict[node_cost] = [path_till_node]
    else:
        path_dict[node_cost].append(path_till_node)
    return path_dict

def A_star_Traversal(cost, heuristic, start_point, goals):

    # Parameters
    n = len(cost)                                               # Number of Nodes in Graph
    visited = [0 for i in range(n)]                             # Visited Set (0 - not visited, 1 - visited)
    frontier_priority_queue = queue.PriorityQueue()             # Frontier Priority Queue
    
    #A_star_all_paths = dict()                                   # Dictionary of all paths from every start state to goal state

    # Insert (estimated_total_cost, (start_point, A*_path_till_start_node, 0)) into priority queue
    frontier_priority_queue.put((heuristic[start_point], ([start_point], start_point, 0)))

    # Until priority queue is not empty
    while(frontier_priority_queue.qsize() != 0):

        # Pop the node information from the priority queue
        total_estimated_cost, nodes_tuple = frontier_priority_queue.get()
        A_star_path_till_node = nodes_tuple[0]
        node = nodes_tuple[1]
        node_cost = nodes_tuple[2]

        # If the node was not visited
        if visited[node] == 0:
            visited[node] = 1

            # If node is a goal_point, return the A* Path till Goal Node
            if node in goals:
                #A_star_all_paths = path_list_append(A_star_all_paths, total_estimated_cost, A_star_path_till_node)
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
                    frontier_priority_queue.put((estimated_total_cost, (A_star_path_till_neighbour_node, neighbour_node, total_cost_till_node)))

    return list()


def UCS_Traversal(cost, start_point, goals):

    # Parameters
    n = len(cost)                                               # Number of Nodes in Graph
    visited = [0 for i in range(n)]                             # Visited Set (0 - not visited, 1 - visited)
    frontier_priority_queue = queue.PriorityQueue()             # Frontier Priority Queue
    
    # Insert (0, (start_point, UCS_path_till_start_point)) into priority queue
    frontier_priority_queue.put((0, ([start_point], start_point)))

    # Until priority queue is not empty
    while(frontier_priority_queue.qsize() != 0):

        # Pop the node information from the priority queue
        node_cost, nodes_tuple = frontier_priority_queue.get()
        ucs_path_till_node = nodes_tuple[0]
        node = nodes_tuple[1]

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
                        frontier_priority_queue.put((total_cost_till_node, (ucs_path_till_neighbour_node, neighbour_node)))
                                  
    return list()


def DFS_Traversal(cost, start_point, goals):

    # Parameters
    n = len(cost)                                  # Number of Nodes in Graph
    visited = [0 for i in range(n)]                # Visited Set (0 - not visited, 1 - visited)
    frontier_stack = queue.LifoQueue()             # Frontier Stack

    # Insert start_point into stack
    frontier_stack.put((start_point, [start_point]))

    # Until stack is not empty
    while(frontier_stack.qsize() != 0):

        # Pop the node information from the stack
        node, dfs_path_till_node = frontier_stack.get()

        # If the node was not visited
        if visited[node] == 0:
            visited[node] = 1

            # If node is a goal_point, return the DFS Path till Goal Node
            if node in goals:
                return dfs_path_till_node

            # For every neighbour connected node
            # (taken from n-1 to 1, to get first lexicological path)
            for neighbour_node in range(n-1, 0, -1):
                # Connected node has cost > 0
                if cost[node][neighbour_node] > 0:
                    # If the connected node is not visited, insert it into the stack
                    if visited[neighbour_node] == 0:
                        # Add the neighbour node to the new dfs path list
                        dfs_path_till_neighbour_node = copy.deepcopy(dfs_path_till_node)
                        dfs_path_till_neighbour_node.append(neighbour_node)
                        # Insert ((neighbour_node, DFS_path_till_neighbour_node)) into the stack
                        frontier_stack.put((neighbour_node, dfs_path_till_neighbour_node))

    return list()


def tri_traversal(cost, heuristic, start_point, goals):

    l = []

    t1 = DFS_Traversal(cost, start_point, goals)
    t2 = UCS_Traversal(cost, start_point, goals)
    t3 = A_star_Traversal(cost, heuristic, start_point, goals)

    l.append(t1)
    l.append(t2)
    l.append(t3)

    return l
