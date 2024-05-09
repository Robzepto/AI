def dfs(maze,start,end):
  stack=[(start,[start])]
  visited=set()
  while stack:
    current,path=stack.pop()
    if current==end:
      return path
    visited.add(current)
    for neighbor in get_neighbors(current,maze):
      if neighbor not in visited:
        stack.append((neighbor,path+[neighbor]))
  return[]

def bfs(maze,start,end):
  queue=[(start,[start])]
  visited=set()
  while queue:
    current,path=queue.pop(0)
    if current==end:
      return path
    visited.add(current)
    for neighbor in get_neighbors(current,maze):
      if neighbor not in visited:
        queue.append((neighbor,path+[neighbor]))
  return[]

def get_neighbors(cell,maze):
  x,y=cell
  neighbors=[(x+dx,y+dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]]
  return [(nx,ny) for nx,ny in neighbors if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]!='#']


maze = [
    ['S', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '.', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'E']
]
start=(0,0)
end=(2,8)
dfs_path=(dfs(maze,start,end))
bfs_path=(bfs(maze,start,end))
print(dfs_path)
print(bfs_path)
