import sys

def fill(containers, goal, fill_amount):
    if containers[0][0] == goal:
        return fill_amount
    else:
        min_val = 10000000
        for x in range(0, len(containers)):
            for y in range(1, len(containers)):
                # moving from x to y
                adding_amount = min(containers[y][1] - containers[y][0], containers[x][1])
                new_containers = list(containers)
                new_containers[x][1] -= adding_amount
                new_containers[y][1] += adding_amount
                min_val = min(min_val, fill(new_containers, goal, fill_amount+adding_amount))
                # moving from y to x
                adding_amount = min(containers[x][1] - containers[x][0], containers[y][1])
                new_containers = list(containers)
                new_containers[y][1] -= adding_amount
                new_containers[x][1] += adding_amount
                min_val = min(min_val, fill(new_containers, goal, fill_amount+adding_amount))
        return min_val

arr = []
for line in sys.stdin:
    arr = line.split()
    arr = [int(e) for e in arr]
containers = arr[1:arr[0]+1]
goal = arr[-1]
containers.sort()
containers.reverse()
filled_containers = [[containers[0], containers[0]]]
for container in containers[1:]:
    filled_containers.append([container,0])
print('filled containers', filled_containers)
min_level = fill(filled_containers, goal, 0)
