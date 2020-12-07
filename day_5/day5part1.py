# For example, consider just the first seven characters of FBFBBFFRLR:
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.

from math import floor, ceil

with open('day5data.txt') as datafile:
    boardingid = datafile.readlines()

loids = []
for id in boardingid:
    rows = 0
    rows_max = 127
    column = 0
    column_max = 7
    id = id.strip()
    for idx in id:
        if idx == "F":
            rows_max = rows + floor((rows_max - rows)/2)
        elif idx == "B":
            rows += ceil((rows_max - rows)/2)
            # rows = floor(rows_max/2)
        elif idx == "R":
            column = column + ceil((column_max - column)/2)
        elif idx == "L":
            column_max = floor((column_max-column)/2)
    loids.append((rows*8)+column)
    
    # print(f"Col: {column}, Max_column: {column_max}")    
    # print(f"Row: {rows}, Max_rows: {rows_max}; Col: {column}, Max_column: {column_max}")
loids.sort(reverse=True)
print(loids[0])