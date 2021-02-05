import matplotlib.pyplot as plt


def barPrc():
    x = [1, 2, 3]
    y = [2, 2, 3]

    x1 = [1, 4, 6]
    y1 = [1, 1, 5]

    plt.bar(x, y, label="bar 1", color="r")
    plt.bar(x1, y1, label="bar 2", color="g")

    plt.plot(x, y, label="First line")
    plt.plot(x1, y1, label="second line")
    plt.xlabel("Plot Number")
    plt.ylabel("Important var")
    plt.title("Interesting Graph\nCheck it out")
    plt.legend()

    plt.show()
