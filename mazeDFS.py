#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:46:59 2018

@author: zouhao
Function:
    DFS for maze
"""
from graphics import *
from myarray2d import Array2D
from maze import Maze
from mazedraw improt MazeDraw

def DFS(maze, v, goal, came_from):
    if came_from == {}:
        came_from[v] = None
        
    if v == goal:
        return v
    
    maze[v[0], v[1]] = maze.OCCUPIED
    for w in maze.getAllMoves(v[0], v[1]):
        if maze[w[0], w[1]] == Maze.EMPTY:
            came_from[w] = v
            result = DFS(maze, w, goal, came_from)
            if result == goal:
                return result
    return None

def drawPath(win, maze, came_from):
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    add = lambda x,y:x+y
    current = maze.goal
    while current != maze.start:
        next = came_from[current]
        for offset in offsets:
            next_one = tuple(map(add, current, offset))
            if next_one == next:
                line = Line(Point(next[1]+1+0.5, \
                                  maze.numRows()-next[0]+1-0.5), \
                            Point(current[1]+1+0.5, \
                                  maze.numRows()-current[0]+1-0.5))
                line.setOutline('white')
                line.setArrow('last')
                line.draw(win)
        current = next
        
def main():
    win = GraphWin('DFS for Maze', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    mazedraw = MazeDraw(win, maze)
    mazedraw.draw()
    came_from = {}
    found = DFS(maze, maze.start, maze.goal, came_from)
    text = Text(Point(11, 0.5), ' ')
    if found == maze.goal:
        text.setText('Goal found!')
        drawPath(win, maze, came_from)
    else:
        text.setText('Goal not found!')
    text.draw(win)
    
    while win.checkKey != 'Escape':
        pass
    win.close()
    
if __name__=='__main__':
    main()
