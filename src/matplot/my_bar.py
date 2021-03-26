import numpy as np
import matplotlib.pyplot as plt


def barPrc():
    plt.style.use('fivethirtyeight')
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    x_indexes = np.arange(len(ages_x))
    width = 0.25

    dev_y = [38496, 42000, 46752, 46732, 53200, 56000, 62316, 64928, 67137, 68748, 73752]
    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
    js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

    plt.bar(x_indexes - width, dev_y, width=width, color="#78FDFF", label="bar 1")
    plt.bar(x_indexes, py_dev_y, width=width, color="#FF3D4A", label="bar 2")
    plt.bar(x_indexes + width, js_dev_y, width=width, color="#223D4A", label="bar 2")

    plt.xticks(ticks=x_indexes, labels=ages_x)
    plt.xlabel("Ages")
    plt.ylabel("Median Salary (USD) by Age")
    plt.title("Interesting Graph\nCheck it out")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    barPrc()
