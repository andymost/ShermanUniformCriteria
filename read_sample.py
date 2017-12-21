import numpy as np


def read(path):
    result = np.array([])
    file = open(path, 'r')
    file.readline()
    file.readline()
    for line in file:
        val = float(line)
        result = np.append(result, val)

    file.close()
    return result