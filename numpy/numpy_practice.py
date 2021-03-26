import numpy as np


def createArray():
    a = np.array([1, 2, 3])
    a1 = np.zeros(2, 2)
    a2 = np.ones(2)
    a3 = np.empty(2)
    a4 = np.arange(2, 9, 2)
    a5 = np.linspace(0, 10, 5)
    a6 = np.ones(2, dtype=int)


def operateArray():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    np.append(a, [12, 34])
    np.delete(a, 1)


def arrayInfo():
    array_example = np.array([
        [[0, 1, 2, 3][4, 5, 6, 7]],
        [[0, 1, 2, 3][4, 5, 6, 7]],
        [[0, 1, 2, 3][4, 5, 6, 7]]
    ]
    )

    print(array_example.ndim)
    print(array_example.size)
    print(array_example.shape)
