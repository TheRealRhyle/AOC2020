with open ("day1hint.txt", "r+") as hint:
  lines = hint.readlines()
  
intList = []
  # check if first item + n-item = 2020
for i in lines:
  intList.append(eval(i))

for x in range(len(intList)):
  for y in intList:
    for z in intList:
      if (intList[x] + y + z == 2020):
        print(intList[x])
        print(y)
        print(z)
        print(intList[x] * y * z)
      else:
        pass
