with open ("day3data.txt", "r") as skiroute:
    route = skiroute.readlines()
    route = [ line.strip() for line in route ] 

treeCount = 0
r, c= 0,0

while r+1 < len(route):
    r += 1
    c += 3

    sector = route[r][c % len(route[r])]
    if sector == "#":
        treeCount += 1

print(treeCount)

