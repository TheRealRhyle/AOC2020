with open('day5data.txt') as datafile:
    boardingid = datafile.readlines()

seats = []
for id in boardingid:
    x = id.replace("F", "0").replace("B", "1").replace("R", "1").replace("L","0")
    seats.append(int(x,2))

seats.sort()
for x in range(883):
    if seats[x] + 1 != seats[x+1]:
        print(seats[x]+1)
