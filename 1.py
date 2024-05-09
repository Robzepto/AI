total=int(input("Enter total no of bananas "))
distance=int(input("Enter distance to be covered "))
capacity=int(input("Enter the capacity of camel "))
lose=0
start=total
for i in range(distance):
    while start>0:
        start=start-capacity
        if start==1:
            lose=lose-1
        lose=lose+2
    lose=lose-1
    start=total-lose
    if start==0:
        break
print(start)
