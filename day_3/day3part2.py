with open ("day3data.txt", "r") as skiroute:
    route = skiroute.readlines()
    route = [ line.strip() for line in route ] 

treeCount = 0
r, c= 0,0

s = [(1,1),(3,1),(5,1),(7,1),(1,2)]

total = 1

for slp in s:
    treeCount = 0
    r,c = 0,0

    while r+1 < len(route):
        r += slp[1] 
        c += slp[0]

        sector = route[r][c % len(route[r])]
        if sector == "#":
            treeCount += 1
    total *= treeCount
print(total)

