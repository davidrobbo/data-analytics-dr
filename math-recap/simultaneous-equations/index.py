import matplotlib.pyplot as plt

# Dummy stuff
plt.plot([0, 1], [0, 2])
plt.plot([0, 3], [0, 4])
plt.axis([0, 4, 0, 4])
plt.plot([1.32], [1.76], 'bx', label='point')
plt.title("Vector Projection dummy example")
plt.show()
