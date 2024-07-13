'''
graph.py

Created Jul, 2024

@author: mikejyg
'''
import sys

# a graph is a set of nodeId -> list of connections to other nodeIds
# specifically for maze, a separate paths is used to indicate active connections. 

def _traverse(graph, paths, visitedNodes, tpath, nodeId, prevNodeId=None, stop=None):  # @NoSelf
    visitedNodes.add(nodeId)
    tpath.append(nodeId)
    
    if stop and nodeId==stop:
        return True
    
    for c in graph[nodeId]:
        if (nodeId, c) not in paths:
            continue;
        
        if prevNodeId and c == prevNodeId:   # do not go backwards.
            continue

        if c in visitedNodes:
            raise Exception( "traverse() loop at: ", c );

        if _traverse(graph, paths, visitedNodes, tpath, c, nodeId, stop):
            return True

    tpath.pop()

    return False


# check the maze by traversing it.
#   there shall be no loop.
#   if stop is not provided, check whether all nodes in the graph are visited.
# return True if stop is reached, false otherwise.
# return the path to stop if it is reached.
def traverse(graph, paths, start=None, stop=None):  # @NoSelf
    sys.setrecursionlimit(len(graph))
    
    if not start:
        for n in graph:
            start=n
            break
        
    if start==None:
        return
        
    visitedNodes=set()
    tpath=list()

    k = _traverse(graph, paths, visitedNodes, tpath, start, stop=stop);
    
    if stop==None and len(visitedNodes) != len(graph):
        raise Exception("traverse() not all nodes visited: ", len(visitedNodes), " vs ", len(graph) )

    return k, tpath

