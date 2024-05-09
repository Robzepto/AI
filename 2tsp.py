from sys import maxsize
from itertools import permutations
V=4
def tsp(graph,s):
  vertex=[]
  for i in range(V):
    if i!=s:
      vertex.append(i)
  minpath=maxsize
  min_path_indices=None
  next_perm=permutations(vertex)
  for i in next_perm:
    c=0
    k=s
    for j in i:
      c+=graph[k][j]
      k=j
    c+=graph[k][s]
    if c<minpath:
      minpath=c
      min_path_indices=[s]+list(i)+[s]
  return minpath,min_path_indices
graph=[[0,10,15,20],[10,0,25,35],[15,25,0,30],[20,35,30,0]]
s=0
minweight,min_path_indices=tsp(graph,s)
print("dfsrt",minweight)
print(min_path_indices)
