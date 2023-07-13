from PIL import Image, ImageDraw, ImageColor
import colorsys
import numpy as np

chip_size = 100  # Size of each color chip
gap_size = 20  # Gap between color chips

def create_hue_chart(hue_index):
    hue_value = hue_index * 18.0open

    image_width = chip_size * 12 + gap_size * 11
    image_height = chip_size * 12 + gap_size * 11

    img = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    max_value = 12

    for row in range(12):
        for col in range(12):
            value = max_value - row  # Reverse order for value
            saturation = col / 12.0  # Adjusted saturation range

            h = hue_value / 360.0
            s = saturation
            v = value / max_value

            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            a = 255 if (r, g, b) != (0, 0, 0) else 0

            if np.isnan(r) or np.isnan(g) or np.isnan(b):
                r = g = b = 255
                a = 0

            x = col * (chip_size + gap_size)
            y = row * (chip_size + gap_size)

            # Render white border around NaN color chips
            border_color = (255, 255, 255) if np.isnan(r) or np.isnan(g) or np.isnan(b) else (0, 0, 0)

            # Render color chip
            draw.rectangle([(x, y), (x + chip_size - 1, y + chip_size - 1)], fill=(r, g, b, a))
            draw.rectangle([(x, y), (x + chip_size - 1, y + chip_size - 1)], outline=border_color)

            chip_properties = {
                "H": hue_value,
                "S": saturation,
                "V": value,
                "R": r,
                "G": g,
                "B": b,
                "A": a,
                "image-x-center": x + chip_size // 2,
                "image-y-center": y + chip_size // 2,
            }

            print(chip_properties)

    img.save(f"HSV-{hue_index}.png")

# Generate hue chart images and output color chip properties
for hue_index in range(20):
    create_hue_chart(hue_index)
