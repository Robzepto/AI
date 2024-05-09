from queue import PriorityQueue
def best(graph,start,goal,heuristic):
  visited=set()
  pq=PriorityQueue()
  pq.put((0,start))
  path={start: [start]}
  while not pq.empty():
    cost,current=pq.get()
    if current==goal:
      return path[current]
    visited.add(current)
    for neighbor,neighborcost in graph[current].items():
      if neighbor not in visited:
        priority=heuristic(neighbor,goal)
        pq.put((priority,neighbor))
        path[neighbor]=path[current]+[neighbor]
  return[]

def astar(graph,start,goal,heuristic,cost):
  visited=set()
  pq=PriorityQueue()
  pq.put((0,start))
  path={start: [start]}
  while not pq.empty():
    g,current=pq.get()
    if current==goal:
      return path[current]
    visited.add(current)
    for neighbor,neighborcost in graph[current].items():
      if neighbor not in visited:
        h=heuristic(neighbor,goal)
        f=g+neighborcost+h
        pq.put((f,neighbor))
        path[neighbor]=path[current]+[neighbor]
  return[]


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 1, 'F': 4},
    'D': {'B': 3},
    'E': {'B': 1},
    'F': {'C': 4}
}

def euclidean(node,goal):
  coordinates = {
        'A': (0, 0), 'B': (1, 1), 'C': (2, 0),
        'D': (1, -1), 'E': (2, 1), 'F': (3, 0)
    }
  x1,y1=coordinates[node]
  x2,y2=coordinates[goal]
  return ((x1-x2)**2+(y1-y2)**2)**0.5

start='A'
goal='F'
path_best=best(graph,start,goal,euclidean)
print(path_best)
path_astar=astar(graph,start,goal,euclidean,cost=1)
print(path_astar)
