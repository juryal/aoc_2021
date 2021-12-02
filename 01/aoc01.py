import sys
from collections import deque
def part_one(file):
    depthqueue = deque()
    increases = 0
    for line in file:
        depth = int(line.strip("\r\n"))
        depthqueue.append(depth)
        if len(depthqueue) == 2:
            if depthqueue[0] < depthqueue[1]:
                increases += 1
            depthqueue.popleft()
    return increases


def part_two(file):
    depthqueue = deque()
    sumqueue = deque()
    increases = 0
    for line in file:
        depth = int(line.strip("\r\n"))
        depthqueue.append(depth)
        if len(depthqueue) == 3:
            sumqueue.append(sum(depthqueue))
            if len(sumqueue) == 2:
                if sumqueue [0] < sumqueue[1]:
                    increases += 1
                sumqueue.popleft()
            depthqueue.popleft()
    return increases


    
file = open("data.txt")
mode = 2
if mode == 1:
    print(part_one(file))
if mode == 2:
    print(part_two(file))
