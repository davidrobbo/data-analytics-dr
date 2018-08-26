import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = './output/'
# Add some vectors to a chart
vals = [[0, 0], [1, 1], [2, 2], [3, 3]]
# vals = [[0, 1, 2, 3], [0, 1, 2, 3]] OUTPUT SAME AS ABOVE
#plt.plot(vals)
#plt.show()

# Add title, and axis names
plt.title("Some Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
#plt.show()

# Change axis [xmin, xmax, ymin, ymax]
#plt.axis([0, 10, 0, 20])
#plt.show()

# Change color and line type of plot (3rd argument to plot [default = 'b-'])
#plt.plot([0, 2], [1, 4], 'ro')
#plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles (More examples)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**4, 'b^')
#plt.show()

# Example of categorical variables and subplots
'''
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(16, 4))

plt.subplot(141)
plt.bar(names, values)
plt.subplot(142)
plt.scatter(names, values)
plt.subplot(143)
plt.plot(names, values)
plt.subplot(144)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
'''

# Add text to chart given X and Y co-ordinates
plt.plot([0, 1, 2], [1, 2, 3])
plt.text(1.5, 2, 'Hello World')
plt.show()
