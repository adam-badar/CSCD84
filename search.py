# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from math import ceil
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #initialize stack
    stk = util.Stack()
    path = []
    visited = set()
    #push a tuple onto stack
    stk.push((problem.getStartState(), []))
    while not stk.isEmpty():
        stk_element = stk.pop()
        curr_node = stk_element[0]
        curr_path = stk_element[1]
        if problem.isGoalState(curr_node):
            return curr_path
        if curr_node not in visited:
            visited.add(curr_node)
            successors = problem.getSuccessors(curr_node)
            for i in range(len(successors)):
                if successors[i][0] not in visited:
                    stk.push((successors[i][0], (curr_path + [successors[i][1]])))
    return path


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    path = []
    visited = []
    
    # push a tuple onto the queue
    queue.push((problem.getStartState(), []))
    
    while not queue.isEmpty():
        # pop an element from the queue
        queue_element = queue.pop()
        curr_node = queue_element[0]
        curr_path = queue_element[1]
        if problem.isGoalState(curr_node):
            return curr_path

        if curr_node not in visited:
            visited.append(curr_node)
            successors = problem.getSuccessors(curr_node)
            for i in range(len(successors)):
                successor_state = successors[i][0]
                states_in_queue = []
                for state in queue.list:
                    states_in_queue.append(state[0])
                successor_in_queue = False
                for state in states_in_queue:
                    if successor_state == state:
                        successor_in_queue = True
                        break
                successor_in_visited = False
                for state in visited:
                    if successor_state == state:
                        successor_in_visited = True
                        break
                if successor_in_visited or successor_in_queue:
                    continue
                queue.push((successor_state, (curr_path + [successors[i][1]])))

    return path

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    visited = set()
    pq.push((problem.getStartState(), [], 0), 0)
    while not pq.isEmpty():
        pq_element = pq.pop()
        curr_node = pq_element[0]
        curr_path = pq_element[1]
        curr_cost = pq_element[2]
        if (problem.isGoalState(curr_node)):
            return curr_path
        if curr_node not in visited:
            visited.add(curr_node)
            successors = problem.getSuccessors(curr_node)
            for successor, action, step_cost in successors:
                if successor not in visited:
                    next_path = curr_path + [action]
                    next_cost = curr_cost + step_cost
                    pq.push((successor, next_path, next_cost), next_cost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def manhattanHeuristic(state, problem: SearchProblem):
    return 

def aStarSearch(problem: SearchProblem, heuristic=manhattanHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    visited = []
    pq.push((problem.getStartState(), [], 0), 0)
    while not pq.isEmpty():
        pq_element = pq.pop()
        curr_node = pq_element[0]
        curr_path = pq_element[1]
        curr_cost = pq_element[2]
        if (problem.isGoalState(curr_node)):
            return curr_path
        # if curr_node not in visited:
        #     visited.add(curr_node)
        #     successors = problem.getSuccessors(curr_node)
        #     for successor, action, step_cost in successors:
        #         if successor not in visited:
        #             next_path = curr_path + [action]
        #             next_cost = curr_cost + step_cost
        #             pq.push((successor, next_path, next_cost), next_cost + heuristic(successor, problem))
        if curr_node not in visited:
            visited.append(curr_node)
            successors = problem.getSuccessors(curr_node)
            for i in range(len(successors)):
                successor_state = successors[i][0]
                states_in_queue = []
                for state in pq.heap:
                    states_in_queue.append(state[0])
                successor_in_queue = False
                for state in states_in_queue:
                    if successor_state == state:
                        successor_in_queue = True
                        break
                successor_in_visited = False
                for state in visited:
                    if successor_state == state:
                        successor_in_visited = True
                        break
                if successor_in_visited or successor_in_queue:
                    continue
                next_path = curr_path + [successors[i][1]]
                next_cost = curr_cost + successors[i][2]
                pq.push((successors[i][0], next_path, next_cost ), next_cost + heuristic(successors[i][0], problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
