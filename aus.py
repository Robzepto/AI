def color_australia():
  australia_map={
      'WT': ['NT','SA'],
      'NT':['WA','SA','Q'],
      'SA':['WA','NT','Q','NSW','V'],
      'Q':['NT','SA','NSW'],
      'NSW':['Q','SA','V'],
      'V':['SA','NSW']
  }
  colors=['red','green','yellow']
  color_assignment={}
  for region in australia_map:
    neighbor_colors=set(color_assignment.get(neighbor,None)for neighbor in australia_map[region])
    for color in colors:
      if color not in neighbor_colors:
        color_assignment[region]=color
        break
  for region,color in color_assignment.items():
    print(f'{region}:{color}')
color_australia()
