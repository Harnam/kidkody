import sys
print(sys.argv)
kky = open(sys.argv[1], "r")
f = kky.read()
kky.close()
print(f)