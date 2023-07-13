import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import colour

# List of Munsell hues
hues = ["5R", "10R", "5YR", "10YR", "5Y", "10Y", "5GY", "10GY", "5G", "10G",
        "5BG", "10BG", "5B", "10B", "5PB", "10PB", "5P", "10P", "5RP", "10RP"]

# Generate a grid of chroma and value coordinates
chroma = np.linspace(0, 14, 15)  # chroma varies from 2 to 14 in steps of 1
value = np.linspace(1, 9, 9)  # value varies from 1 to 9 in steps of 1

for index, hue in enumerate(hues, start=1):
    # Create a 2D grid of colors
    colors = np.zeros((9, 15, 4))

    # Calculate the RGBA values for each square
    for i, v in enumerate(value):
        for j, c in enumerate(chroma):
            try:
                # Convert the Munsell color to xyY using the colour-science library
                xyY = colour.munsell_colour_to_xyY("%s %.1f/%.1f" % (hue, v, c))

                # Convert the xyY color to sRGB for visualization
                sRGB = colour.XYZ_to_sRGB(colour.xyY_to_XYZ(xyY))

                # Clip the sRGB values to the valid range [0, 1]
                sRGB = np.clip(sRGB, 0, 1)

                # set the RGB and alpha channels
                colors[i, j, :3] = sRGB
                colors[i, j, 3] = 1.0  # fully opaque
            except ValueError:
                # If the Munsell color is not in the dataset, set to transparent
                colors[i, j] = [0, 0, 0, 0]  # fully transparent

    # invert the y-axis
    colors = np.flip(colors, axis=0)

    # Expand the grid to create space between squares and for 100x100 pixel squares
    expanded_colors = np.zeros((900+8*20, 1300+12*20, 4))
    for i in range(9):
        for j in range(13):
            expanded_colors[i*120:(i*120)+100, j*120:(j*120)+100] = colors[i, j]

    # Convert the array to an image
    img = Image.fromarray(np.uint8(expanded_colors*255))

    # Save the image
    file_name = f"munsell-{index:02}-chart-{hue}.png"
    img.save(file_name, dpi=(72, 72))
    print(f"Saved {file_name}")
