from Assignment2 import *


def test_case():
    '''size of cost matrix is 11x11
    0th row and 0th column is ALWAYS 0
    Number of nodes is 10
    size of heuristic list is 11
    0th index is always 0'''

    cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
            [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
            [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
            [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
            [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
            [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
            [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
            [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
    heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]

    try:
        # start node is 1, goal states to reach are 6,7 & 10
        if (tri_traversal(cost,heuristic, 1, [6, 7, 10]))[0] == [1, 2, 3, 4, 7]:
            print("SAMPLE TEST CASE 1 FOR THE  DFS_TRAVERSAL PASSED")
        else:
            print("SAMPLE TEST CASE 1 FOR THE  DFS_TRAVERSAL FAILED")
    except:
        print("SAMPLE TEST CASE 1 FOR THE DFS_TRAVERSAL FAILED")
    try:
        if (tri_traversal(cost,heuristic, 1, [6, 7, 10]))[1] == [1, 5, 4, 7]:
            print("SAMPLE TEST CASE 2 FOR THE  UCS_TRAVERSAL PASSED")
        else:
            print("SAMPLE TEST CASE 2 FOR THE  UCS_TRAVERSAL FAILED")
    except:
        print("SAMPLE TEST CASE 2 FOR THE UCS_TRAVERSAL FAILED")

    try:
        if (tri_traversal(cost,heuristic, 1, [6, 7, 10]))[2] == [1, 5, 4, 7]:
            print("SAMPLE TEST CASE 3 FOR THE  A_star_TRAVERSAL PASSED")
        else:
            print("SAMPLE TEST CASE 3 FOR THE  A_star_TRAVERSAL FAILED")
    except:
        print("SAMPLE TEST CASE 3 FOR THE A_star_TRAVERSAL FAILED")


test_case()