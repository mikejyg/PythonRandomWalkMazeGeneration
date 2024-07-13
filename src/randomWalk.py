'''
randomWalk.py

Created Jul, 2024

@author: mikejyg
'''
from random import randrange
from graph import traverse

# this function does not modify nodes
def randomWalk(graph, verify=True):
    maze=set()  # a set of node IDs
    paths=set() # a set of node ID pairs
    
    loopEraseCnt=0
    walkCnt=0
    
    for n in graph:
        if n in maze:
            continue
        walk=[n] # a list of node IDs
        walkMap={n:0}
        while True:
            connections=graph[ walk[-1] ]
            c=randrange( len(connections) )
            n1Id=connections[c]
            if n1Id in maze:
                walk.append(n1Id)
                break
            
            if len(walk)>=2:
                # check whether it is going backwards
                if walk[len(walk)-2] == n1Id:
                    continue
            
            if n1Id in walkMap:
                if not maze:
                    break;
                else:
                    # remove loop
                    idx=walkMap[n1Id]
                    idx+=1
                    for i in range(idx, len(walk)):
                        del walkMap[walk[i]]
                    del walk[idx:]
                    loopEraseCnt += 1
                    continue
            else:
                walk.append(n1Id)
                walkMap[n1Id]=len(walk)-1

        #  move walk to maze
        if not maze:
            maze.add(walk[-1])
        for i in range(len(walk)-1):
            n=walk[i]
            nextNode=walk[i+1]
            paths.add((n, nextNode));
            paths.add((nextNode, n));
            maze.add(n)
        
        walkCnt+=1
        walk.clear()
        walkMap.clear()
    
    # sanity check
    if len(maze) != len(graph):
        raise Exception("randomWalk() ERROR: not all nodes are in the maze.")

    if verify:
        traverse(graph, paths)
            
    return paths, walkCnt, loopEraseCnt

