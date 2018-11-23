# DFS-BFS-in-Maze
Depth-First-Search &amp; Breadth-First-Search in finding the optimal path of labyrinth.
# Breadth-First-Search(BFS)
There two ways in implementing BFS algorithms: Queue & OPEN-CLOSED table.
## Queue
```
Input:
  A graph G and a vertex v of G
  came_from is a DICT, initialized with {}
Output:
  return: GOAL or None
  came_from is changed
def BFS(G, V, came_from):
  frontier = Queue()
  frontier.enqueue(v)
  came_from[v] = None
  while not frontier.is_empty():
    v = frontier.dequeue()
    if v is not labeled as discovered:
      if v is a goal:
        return v
      else:
        label v as discovered
        for all edges from v to w in G.adjacentEdges(v):
          if w is not labeled as discovered:
            frontier.enqueue(w)
            came_from[w] = v
  return None
```
## OPEN-CLOSED
```
Input:
  A graph G and a vertex v of G
  came_from is a DICT, initialized with {}
Output:
  return: GOAL or None
  came_from is changed
def BFS(G, V, came_from):
  open = [v]
  closed = []
  came_from[v] = None
  while open is not empty:
    remove an element from the front of open, call it v
    if v is a goal:
      return v
    else:
      put v on closed
      for all edges from v to w in G.adjacentEdges(v):
        if w is not in closed:
          put w at the back of open
          came_from[w] = v
  return None
```

# Depth-First-Search（DFS）
There two ways in implementing DFS algorithms: Recursive & Non-recursive.
## Recursive algorithm in DFS
```
Input:
  A graph G and a vertex v of G
  came_from is a DICT, initialized with {}
Output:
  return: GOAL or None
  came_from is changed
def DFS(G, V, came_from):
  if came_from == {}:
    came_from[v] = None
  if v is a goal:
    return v
  label v as discovered
  for all edges from v to w in G.adjacentEdges(v):
    if vertex w is not labeled as discovered:
      came_from[w] = v
      result = DFS(G, W, came_from)
      if result is a goal:
        return result
  return None
```
## Non-recursive algorithms in DFS
```
Input:
  A graph G and a vertex v of G
  came_from is a DICT, initialized with {}
Output:
  return: GOAL or None
  came_from is changed
def DFS(G, V, came_from):
  frontier = Stack()
  frontier.push(v)
  came_from[v] = None
  while not frontier.is_empty():
    v = frontier.pop()
    if v is not labeled as discovered:
      if v is a goal:
        return v
      else:
        label v as discovered
        for all edges from v to w in G.adjacentEdges(v):
          frontier.push(w)
          came_from[w] = v
  return None
```
