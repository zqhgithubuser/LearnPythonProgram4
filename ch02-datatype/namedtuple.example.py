from collections import namedtuple

Vision = namedtuple("Vision", ["left", "combined", "right"])
vision = Vision(9.5, 9.2, 8.8)
print(vision.left)
print(vision.right)
print(vision.combined)
