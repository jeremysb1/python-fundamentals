fh = open('fear.txt')
try:
    for line in fh:
        print(line.strip())
finally:
    fh.close()