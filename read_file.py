#this program is to test file operations
#<calss '_io.TextIOWrapper'>

lines = []

f = open("myfile.txt", "r")

for line in f:
    line = line.strip()
    lines.append(line)
    print(line)

f.close()

print(len(lines))