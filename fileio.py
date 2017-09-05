import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'+ 'fileio.txt'
print(dir_path)

f = open(dir_path, 'w')
for i in range(1, 11):
    data = "%d line.\n" % i
    f.write(data)
f = open(dir_path, 'rb')
line = f.readline()
while len(line) is not 0:
    print(line, len(line))
    line = f.readline()

f.close()