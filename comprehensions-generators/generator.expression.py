cubes = [k**3 for k in range(10)]
print(cubes)

cubes_gen = (k**3 for k in range(10))
print(cubes_gen)

print(list(cubes_gen))