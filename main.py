import sys
print(sys.argv)
kky = open(sys.argv[1], "r")
f = kky.read()
kky.close()
print(f)

s = []
word = ""
for x in f:
    if x == '.':
        s.append(word)
        word = ""
    else:
        word += x

print(s)