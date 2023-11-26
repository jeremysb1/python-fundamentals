sq1 = list(map(lambda n: n **2, filter(lambda n: not n % 2, range(10))))
sq2 = [n ** 2 for n in range(10) if not n % 2]

print(sq1, sq1==sq2)