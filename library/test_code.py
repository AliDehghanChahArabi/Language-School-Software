import os
import glob
x = "ali"
os.chdir("../students")
for file in glob.glob(x):
    if x == file:
        print ("ok")
if x != file:
    print ("no")
