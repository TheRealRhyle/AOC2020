#
# Advent of Code
# 2020, Day 2 part 1.
#

# sample line from data file.
# 5-6 d: jdddqqt

correctcounter = 0

with open ("day2data.txt", "r") as data:
  for line in data:
    num, alpha, password =  line.split(" ")
    alpha = alpha.replace(":", "")
    min, max =  num.split("-")
    min = int(min)
    max = int(max)
#    print(f'{password.count(alpha)} {min} {max}')
    if password.count(alpha) >= min and password.count(alpha) <= max:
      print(password)
      correctcounter += 1

print(correctcounter)


