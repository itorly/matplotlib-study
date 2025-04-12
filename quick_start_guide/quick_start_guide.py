import matplotlib.pyplot as plt
import numpy as np
# # 1 Quick start guide
# # 1.1 A simple example
# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                           # Show the figure.
#
# # 1.2 Parts of a Figure
# # 1.2.1 The Figure
# fig = plt.figure()             # an empty figure with no Axes
# fig, ax = plt.subplots()       # a figure with a single Axes
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# # a figure with one Axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                ['left', 'right_bottom']])
#
# plt.show()

# 1.3 Types of inputs to plotting functions
# b = np.matrix([[1, 2], [3, 4]])
# b_asarray = np.asarray(b)
# print('b_asarray=\n', b_asarray)

# np.random.seed(19680801)  # seed the random number generator.
# data = {
#     # 50 values from 0 to 49
#     'a': np.arange(50),
#     # 50 random integers between 0 and 49
#     'c': np.random.randint(0, 50, 50),
#     # 50 random values from a standard normal distribution
#     'd': np.random.randn(50)
# }
# # Adds a fourth array 'b' which is 'a' plus some random noise (scaled by 10)
# data['b'] = data['a'] + 10 * np.random.randn(50)
# # Modifies 'd' to be absolute values multiplied by 100 (these will be used for marker sizes)
# data['d'] = np.abs(data['d']) * 100
# # Creates a figure and axes (plot area) with:
# # Size 5 inches wide × 2.7 inches tall
# # 'constrained' layout to prevent label overlapping
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# # Creates a scatter plot where:
# # x-values come from data['a']
# # y-values come from data['b']
# # Colors (c) come from data['c']
# # Marker sizes (s) come from data['d']
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# # plt.show()


# 1.4 Coding styles
# 1.4.1 The explicit and the implicit interfaces
x = np.linspace(0, 2, 100)  # Sample data.

# 1.4.1.1 OO-style
# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the Axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the Axes.
ax.set_ylabel('y label')  # Add a y-label to the Axes.
ax.set_title("Simple Plot")  # Add a title to the Axes.
ax.legend()  # Add a legend.
plt.show()