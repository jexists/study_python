# from os import walk

# f = []
# for (dirpath, dirnames, filenmaes) in walk(r"~\Users\jexists\Downloads\images"):
#   f.extend(filenmaes)
#   break
# print(f)

# #from os import walk
import os

fName = []
fSize = []
for (dirpath, dirnames, filenmaes) in walk(r"./images"):
  # f.extend(filenmaes)
  for file in filenmaes:
    fName.append(file)
    fSize.append(os.stat(dirpath + '/' + file).st_size)

  break
print(fName)
print(fSize)
print("test")