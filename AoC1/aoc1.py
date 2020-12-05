filename = "aoc.txt"

with open(filename) as f:
    numbers = list(map(int,f.readlines()))




for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 2020:
                print(x*y*z)
    
