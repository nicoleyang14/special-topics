import os
import sys
print("hi world")
input()
f = open(os.path.join(sys.path[0], "hello.txt"))
print(f.read())
input()
sys.exit()