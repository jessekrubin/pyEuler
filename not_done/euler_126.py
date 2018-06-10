



cubes = 0

print(cubes)



from pprint import pprint


def cuboid_layers(a, b, c):
    c = [[[1]*a]*b]*c
    pprint(c)

    
    
cuboid_layers(3, 2, 1)
cuboid_layers(3, 3, 3)




