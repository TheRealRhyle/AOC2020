#
# Advent of Code
# 2020, Day 2 part 1.
#

# sample line from data file.
# 5-6 d: jdddqqt
# 18-20 v: hbjhmrtwzfqfvhzjjvcv

correctcounter = 0

with open ("day2data.txt", "r") as data:
  for line in data:
    num, alpha, password =  line.split(" ")
    password = password.strip("\r\n")
    alpha = alpha.strip(":")
    pos1, pos2 =  num.split("-")
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1
#    print(f'{password.count(alpha)} {min} {max}')
#    password =  " " + password
#    print(f"{password} {pos1}: {password[pos1]} {pos2}: {password[pos2]}", end="\r\n")
    if password[pos1] == alpha:
      if password[pos2] != alpha:
        correctcounter += 1
    elif password[pos2] == alpha:
      correctcounter += 1

print(correctcounter)


