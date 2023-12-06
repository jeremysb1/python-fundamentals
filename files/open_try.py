fh = open('fear.txt', 'rt')
for line in fh.readlines():
    print(line.strip())
fh.close()