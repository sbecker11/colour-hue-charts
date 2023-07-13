import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

# List of Munsell hues
hues = ["5R", "10R", "5YR", "10YR", "5Y", "10Y", "5GY", "10GY", "5G", "10G",
        "5BG", "10BG", "5B", "10B", "5PB", "10PB", "5P", "10P", "5RP", "10RP"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Load the images and plot them on individual planes in the 3D space
for index, hue in enumerate(hues, start=1):
    img = mpimg.imread(f'munsell-{index:02}-chart-{hue}.png')

    # Create a grid of x, y coordinates
    x = np.linspace(-0.5, 0.5, img.shape[1])
    y = np.linspace(-0.5, 0.5, img.shape[0])

    x, y = np.meshgrid(x, y)

    # Calculate the z coordinates of the points in the plane
    angle = index * 2 * np.pi / 20  # each plane has a different angle
    z = np.zeros_like(x)

    # Assign the image to the plane
    ax.plot_surface(x*np.cos(angle), y, z + x*np.sin(angle), rstride=5, cstride=5, facecolors=img)

plt.show()
