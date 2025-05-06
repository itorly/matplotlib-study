import matplotlib.pyplot as plt
import numpy as np

# # 1 Quick start guide
# # 1.1 A simple example
# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# # plt.show()                           # Show the figure.
# plt.savefig("1.1 A simple example.png")

# 1.2 Parts of a Figure
# 1.2.1 The Figure
# fig = plt.figure()             # an empty figure with no Axes
# fig, ax = plt.subplots()       # a figure with a single Axes
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# # a figure with one Axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                ['left', 'right_bottom']])
#
# # plt.show()
# plt.savefig("1.2 Parts of a Figure.png")

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
# plt.savefig("1.3 Types of inputs to plotting functions.png")


# 1.4 Coding styles
# 1.4.1 The explicit and the implicit interfaces

# 1.4.1.1 OO-style
# x = np.linspace(0, 2, 100)  # Sample data.
# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the Axes.
# ax.set_ylabel('y label')  # Add a y-label to the Axes.
# ax.set_title("Simple Plot")  # Add a title to the Axes.
# ax.legend()  # Add a legend.
# # plt.show()
# plt.savefig("1.4.1.1 OO-style.png")


# 1.4.1.2 pyplot-style
# x = np.linspace(0, 2, 100)  # Sample data.
#
# plt.figure(figsize=(5, 2.7), layout='constrained')
# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# # plt.show()
# plt.savefig("1.4.1.2 pyplot-style.png")

# 1.4.2 Making a helper functions
# 1.4.2.1 wrap Matplotlib methods
# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph.
#     """
#     # **kwargs is used in function definitions to capture an arbitrary number of keyword arguments (i.e., named arguments) into a dictionary
#     # passing a dictionary as **kwargs to a function is called dictionary unpacking,
#     # and it allows you to expand a dictionary into keyword arguments
#     out = ax.plot(data1, data2, **param_dict)
#     return out
#
# data1, data2, data3, data4 = np.random.randn(4, 6)  # make 4 random data sets
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': '+'})
#
# # plt.show()
# plt.savefig("1.4.2.1 wrap Matplotlib methods.png")


# 1.5 Styling Artists
data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
# fig, ax = plt.subplots(figsize=(5, 2.7))
# x = np.arange(len(data1))
# ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
# l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
# l.set_linestyle(':')
# # plt.show()
# plt.savefig("1.5 Styling Artists.png")

# 1.5.1 Colors
# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
# # plt.show()
# plt.savefig("1.5.1 Colors.png")

# 1.5.2 Linewidths, linestyles, and markersizes
# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.plot(data1, 'o', label='data1')
# ax.plot(data2, 'd', label='data2')
# ax.plot(data3, 'v', label='data3')
# ax.plot(data4, 's', label='data4')
# ax.legend()
# # plt.show()
# plt.savefig("1.5.2 Linewidths, linestyles, and markersizes.png")

# 1.6 Labelling plots

# 1.6.1 Axes labels and text

# mu, sigma = 115, 15
# x = mu + sigma * np.random.randn(10000)
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# # the histogram of the data
# n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)
#
# ax.set_xlabel('Length [cm]')
# # t = ax.set_xlabel('my data', fontsize=14, color='red')
# ax.set_ylabel('Probability')
# ax.set_title('Aardvark lengths\n (not really)')
# ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
# ax.axis([55, 175, 0, 0.03])
# ax.grid(True)
# # plt.show()
# plt.savefig("1.6.1 Axes labels and text.png")

# 1.6.2 Using mathematical expressions in text

# ax.set_title(r'$\sigma_i=15$')

# 1.6.3 Annotations

fig, ax = plt.subplots(figsize=(5, 2.7))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_ylim(-2, 2)
# plt.show()
plt.savefig("1.6.3 Annotations.png")