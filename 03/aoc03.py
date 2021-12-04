import sys
from os import path

def oxygen_filter(report):
    if len(report) == 1:
        return report[0]
    ones_list =  [x[1:] for x in report if int(x[0]) % 2]

    if len(ones_list) >= len(report) / 2:
        return "1"+ oxygen_filter(ones_list)
    else:
        zeroes_list = [x[1:] for x in report if not int(x[0]) % 2]
        return "0" + oxygen_filter(zeroes_list)

def carbon_filter(report):
    if len(report) == 1:
        return report[0]
    zeroes_list = [x[1:] for x in report if not int(x[0]) % 2]
    
    if len(zeroes_list) <= len(report) / 2:
        return "0"+ carbon_filter(zeroes_list)
    else:
        ones_list =  [x[1:] for x in report if int(x[0]) % 2]
        return "1" + carbon_filter(ones_list)

def part_one(file):
    columntotals = [int(x) for x in file[0].strip("\r\n")]
    readings = 1
    for line in file:
        line = line.strip("\r\n")
        numbers = [int(x) for x in line]
        columntotals = [a + b for a,b in zip(numbers,columntotals)]
        readings += 1
    gamma = '0b' + ''.join([str(1) if columntotals[a] > (readings / 2) else str(0) for a in range(0,len(columntotals))])
    epsilon = '0b' + ''.join([str(1) if columntotals[a] < (readings / 2) else str(0) for a in range(0,len(columntotals))])    
    return (int(gamma, 2) * int(epsilon, 2))

def part_two(file):
    columntotals = [int(x) for x in file.readline().strip("\r\n")]
    readings = 1
    for line in file:
        line = line.strip("\r\n")
        numbers = [int(x) for x in line]
        columntotals = [a + b for a,b in zip(numbers,columntotals)]
        readings += 1


script_dir = path.dirname(__file__)
relative_path = "/data.txt"
file = open(script_dir + relative_path)
mode = 1
blork = [line.strip("\r\n") for line in file]

if mode == 1:
    print(part_one(blork))


print(int("0b" + oxygen_filter(blork),2)*int("0b" + carbon_filter(blork),2))

#if mode == 2:
#    print(part_two(file))
