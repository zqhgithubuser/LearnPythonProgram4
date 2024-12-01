cubes = [k**3 for k in range(10)]
print(cubes)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(type(cubes))  # <class 'list'>

cubes_gen = (k**3 for k in range(10))
print(cubes_gen)
print(type(cubes_gen))  # <class 'generator'>
print(list(cubes_gen))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(list(cubes_gen))  # []
