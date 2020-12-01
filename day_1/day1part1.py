with open ("day1hint.txt", "r+") as hint:
  lines = hint.readlines()
  
intList = []
  # check if first item + n-item = 2020
for i in lines:
  intList.append(eval(i))

for x in range(len(intList)):
  for itm in intList:
    if (intList[x] + itm == 2020):
      print(intList[x])
      print(itm)
      print(intList[x] * itm)
    else:
      pass
