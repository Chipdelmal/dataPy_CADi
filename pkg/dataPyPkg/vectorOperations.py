def scaleVector(scale=1, b=[0]):
    return [i*scale for i in b]


if __name__ == '__main__':
    scaleVector(10, [1, 2, 3])
