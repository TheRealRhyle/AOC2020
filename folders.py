#
#
#	Python create folders
#
#

import os

with open('README.md', 'a') as readme:
  for x in range(1, 25):
    if not os.path.exists("day_" + str(x)):
      os.makedirs("day_" + str(x))
    readme.write("[Day " +str(x) + "[(/" + str(x) + ")\n")
