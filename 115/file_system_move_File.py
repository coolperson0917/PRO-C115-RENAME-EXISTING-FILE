import os
source = 'main.txt'
dest = 'newfile.txt'
os.rename(source,dest)
print("source replaced with destination file name")