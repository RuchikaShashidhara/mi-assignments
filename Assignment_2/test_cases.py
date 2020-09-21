from Assignment2 import *

def print_test_cases(cost, heuristic, start_node, goal_nodes):
    print("DFS", DFS_Traversal(cost, start_node, goal_nodes))
    print("UCS", UCS_Traversal(cost, start_node, goal_nodes))
    print("A* ", A_star_Traversal(cost, heuristic, start_node, goal_nodes))
    print()
    print("tri", tri_traversal(cost, heuristic, start_node, goal_nodes))
    print()
    print()



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

    print("Test case 1\n")
    print_test_cases(cost, heuristic, 1, [6,7,10])


def test_case2():

    cost = [ [0,0,0,0,0,0,0],

             [0,0,2,0,0,10,7],

             [0,0,0,3,0,0,0],

             [0,0,0,0,2,0,2],

             [0,0,0,0,0,3,0],

             [0,0,0,0,0,0,0],

             [0,0,0,0,0,3,0]]

    heuristic = [0 for i in range(7)]

    print("Test case 2\n")
    print_test_cases(cost, heuristic, 1, [5])


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

    print("Test case 3\n")
    print_test_cases(cost, heuristic, 1, [4,7])


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

    print("Test case 4\n")
    print_test_cases(cost, heuristic, 8, [5,7])



test_case1()
test_case2()
test_case3()
test_case4()