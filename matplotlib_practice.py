import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [1, 2, 3]

x1 = [1, 2, 3]
y1 = [2, 2, 5]

plt.plot(x, y, label = "First line")
plt.plot(x1, y1, label = "second line")
plt.xlabel("Plot Number")
plt.ylabel("Important var")
plt.title("Interesting Graph\nCheck it out")
plt.legend()

plt.show()
