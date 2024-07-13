#!/usr/bin/env python3

'''
mazeMain.py

Created Jul, 2024

@author: mikejyg
'''

from mazeDrawer import MazeDrawer
from randomWalk import randomWalk
import random
import argparse
from rectMaze import RectMaze
import ast
from graph import traverse


def loadRectMaze(filename="rectMaze.txt"):
    f = open(filename, 'r')
    g=RectMaze(1,1)
    g.load(f)
    pathsStr=f.readline()
    paths=ast.literal_eval(pathsStr)
    f.close()
    
    return g, paths


def saveRectMaze(mazeGraph, p, filename="rectMaze.txt"):
    f = open(filename, 'w')
    mazeGraph.save(f)
    f.write(repr(p))
    f.write("\n")
    f.close()


if __name__ == "__main__":
    # process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--draw_walls', action='store_true', help='draw maze as walls.') 
    parser.add_argument('-p', '--draw_paths', action='store_true', help='draw maze as paths.')
    parser.add_argument('-x', '--width', help='maze width')
    parser.add_argument('-y', '--height', help='maze height')
    parser.add_argument('-q', '--no_wait_for_close', action='store_true')
    parser.add_argument('-b', '--built_in_test', action='store_true')
    parser.add_argument('-r', '--seed', help='set random seed')
    parser.add_argument('-l', '--load_file', help='load maze from a file.')
    parser.add_argument('-s', '--save_file', help='save maze to a file.')
    parser.add_argument('-f', '--find_path', help='find path between 2 nodes, as x1,y1,x2,y2.')
    
    args = parser.parse_args()
    print(args)

    if args.width:
        w=int(args.width)
    else:
        w=30
        
    if args.height:
        h=int(args.height)
    else:
        h=20

    if args.no_wait_for_close:
        wait=False
    else:
        wait=True
    
    if args.seed:
        random.seed(int(args.seed))

    if args.built_in_test:
        random.seed(1)
        log=True
        wait=False
    else:
        log=False

    if args.load_file:
        mazeGraph, p = loadRectMaze(args.load_file)
        print("loaded maze from file:", args.load_file)

    else:
        # generate a maze.
        print("width:", w, ", height:", h)
        
        mazeGraph=RectMaze(w,h)
        p,walkCnt,loopEraseCnt = randomWalk(mazeGraph.graph)
        
        print("maze is ready. walkCnt:", walkCnt, ", loopEraseCnt:", loopEraseCnt)
        
        # the following can be read to restore the maze.
        if log:
            mazeGraph.printRepr()
            
            # print("paths:")
            print(repr(p))

    if args.save_file:
        saveRectMaze(mazeGraph, p, args.save_file)
        print("saved maze to file:", args.save_file)
    
    if args.find_path:
        xyxy=args.find_path.split(',')
        n1=(int(xyxy[0]),int(xyxy[1]))
        n2=(int(xyxy[2]),int(xyxy[3]))
        print("find path:", n1, n2)
        k,p1=traverse(mazeGraph.graph, p, start=n1, stop=n2)
        if k:
            print(p1)
        else:
            print("no path found.")
    
    d=MazeDrawer()
        
    if args.draw_walls:
        wwait=wait
        if args.draw_paths: # do not wait twice
            wwait=False
        d.drawWalls(mazeGraph, p, wait=wwait)

    if args.draw_paths:
        if args.find_path and k:
            d.drawPaths(mazeGraph, p1, wait=wait)
        else:
            d.drawPathsSet(mazeGraph, p, wait=wait)
