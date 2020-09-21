from Assignment2 import *

def print_test_cases(cost, heuristic, start_node, goal_nodes):
    all_paths = tri_traversal(cost, heuristic, start_node, goal_nodes)
    print("DFS", all_paths[0])
    print("UCS", all_paths[1])
    print("A* ", all_paths[2])
    print()


# Sample test case given for the assignment
def test_case1():
            #0  #1  #2  #3  #4  #5  #6  #7  #8  #9 #10
    cost = [[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # 0
            [0,  0,  5,  9, -1,  6, -1, -1, -1, -1, -1], # 1
            [0, -1,  0,  3, -1, -1,  9, -1, -1, -1, -1], # 2
            [0, -1,  2,  0,  1, -1, -1, -1, -1, -1, -1], # 3
            [0,  6, -1, -1,  0, -1, -1,  5,  7, -1, -1], # 4
            [0, -1, -1, -1,  2,  0, -1, -1, -1,  2, -1], # 5
            [0, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1], # 6
            [0, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1], # 7
            [0, -1, -1, -1, -1,  2, -1, -1,  0, -1,  8], # 8
            [0, -1, -1, -1, -1, -1, -1, -1, -1,  0,  7], # 9
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0]] #10

                #0 #1 #2 #3 #4 #5 #6 #7 #8 #9 #10
    heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]

    print("Test case 1")
    print_test_cases(cost, heuristic, 1, [6,7,10])

# Paths 1->5 and 1->2->3->4->5 are both valid
def test_case2():

    cost = [ [0,0,0,0,0,0,0],

             [0,0,2,0,0,10,7],

             [0,0,0,3,0,0,0],

             [0,0,0,0,2,0,2],

             [0,0,0,0,0,3,0],

             [0,0,0,0,0,0,0],

             [0,0,0,0,0,3,0]]

    heuristic = [0 for i in range(8)]

    print("Test case 2")
    print_test_cases(cost, heuristic, 1, [5])

# No path from one of the nodes
def test_case3():

    cost = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,1],
            [0,1,1,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,0,0,0]]

    heuristic = [0 for i in range(10)]

    print("Test case 3")
    print_test_cases(cost, heuristic, 1, [4,7])

# No path from start node to any goal node
def test_case4():

            #0  #1  #2  #3  #4  #5  #6  #7  #8  #9 #10
    cost  =[[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # 0
            [0,  0, -1,  2,  2, -1, -1, -1, -1, -1, -1], # 1
            [0, -1,  0, -1, -1,  4,  3, -1, -1, -1, -1], # 2
            [0, -1, -1,  0,  5, -1, -1,  2, -1, -1, -1], # 3
            [0, -1, -1, -1,  0, -1, -1,  1, -1, -1, -1], # 4
            [0, -1, -1, -1,  4,  0, -1, -1, -1, -1, -1], # 5
            [0, -1, -1, -1, -1,  6,  0,  3, -1, -1, -1], # 6
            [0, -1,  7, -1, -1, -1, -1,  0, -1, -1, -1], # 7
            [0, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1], # 8
            [0, -1, -1, -1, -1, -1, -1, -1, -1,  0, -1], # 9
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0]] #10

    heuristic = [0 for i in range(11)]

    print("Test case 4")
    print_test_cases(cost, heuristic, 8, [5,7])

# Paths 1->3 and 1->2->3 are both valid
def test_case5():

    cost = [[0, 0, 0, 0],
            [0, 0, 5, 10],
            [0, -1, 0, 5],
            [0, -1, -1, 0]]

    heuristic = [0, 0, 0, 0]

    print("Test case 5")
    print_test_cases(cost,heuristic, 1, [3])

def test_case6():

            #0  #1  #2  #3  #4  #5  #6  #7  #8  #9 #10
    cost  =[[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # 0
            [0,  0, -1,  6, -1, -1, -1, -1, -1, -1, -1], # 1
            [0,  2,  0, -1, -1, -1, -1,  2, -1, -1, -1], # 2
            [0, -1,  2,  0, 10, -1, -1, -1, -1, -1, -1], # 3
            [0, -1, -1, -1,  0, -1, -1,  1, -1, -1, -1], # 4
            [0, -1, -1, -1,  8,  0,  2, -1, -1, -1, -1], # 5
            [0, -1,  3, -1, -1, -1,  0, -1,  6, -1,  7], # 6
            [0, -1, -1, -1, -1, -1,  5,  0, -1, -1, -1], # 7
            [0, -1, -1, -1, -1,  4, -1, -1,  0, 10, -1], # 8
            [0, -1, -1, -1, -1, -1, -1, -1, -1,  0, -1], # 9
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0]] #10

    heuristic = [0 for i in range(11)]

    print("Test case 6")
    print_test_cases(cost, heuristic, 1, [10])


# Start state itself is goal state
def test_case7():

    cost = [[0, 0, 0, 0],
            [0, 0, 5, 10],
            [0, -1, 0, 5],
            [0, -1, -1, 0]]

    heuristic = [0, 0, 0, 0]

    print("Test case 7")
    print_test_cases(cost, heuristic, 1, [1,3])
    
def test_case8():
        cost = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 5, -1, -1, 3, -1],
        [0, -1, 0, -1, -1, 5, -1, -1],
        [0, -1, 3, 0, -1, 5, 7, -1],
        [0, -1, -1, -1, 0, -1, 7, 5],
        [0, 1, 1, -1, -1, 0, 6, 2],
        [0, 3, -1, 3, -1, -1, 0, 4],
        [0, 2, -1, 5, -1, 1, 6, 0 ]]
        
        heuristic = [0, 7, 0, 0, 10, 5, 0, 1]
        
        print("Test case 8")
        print_test_cases(cost, heuristic, 4, [2, 3, 6])
    
def test_case9():  
    
    cost =  [[0,0,0,0,0,0,0,0],
	     [0,0,3,-1,-1,-1,-1,2],
	     [0,-1,0,5,10,-1,-1,-1],
	     [0,-1,-1,0,2,-1,1,-1],
	     [0,-1,-1,-1,0,4,-1,-1],
	     [0,-1,-1,-1,-1,0,-1,-1],
	     [0,-1,-1,-1,-1,3,0,-1],
	     [0,-1,-1,1,-1,-1,4,0]] 

    heuristic = [0 for i in range(8)]

    print("Test case 9")
    print_test_cases(cost, heuristic, 1, [7])



test_case1()
test_case2()
test_case3()
test_case4()
test_case5()
test_case6()
test_case7()
test_case8()
test_case9()
