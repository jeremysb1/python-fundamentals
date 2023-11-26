grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
zips = list(zip(avgs, grades))
print(zips)

maps = list(map(lambda *a: a, avgs, grades))
print(maps)