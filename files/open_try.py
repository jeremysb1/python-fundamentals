fh = open('fear.txt', 'rt')
try:
    for line in fh.readlines():
        print(line.strip())
finally:
    fh.close()