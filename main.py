import colorgram
from PIL import Image

rgb_colors = []
colors = colorgram.extract('image.jpg', 10)  # extract 10 colors from the image
for color in colors:
    rgb_colors.append([color.rgb.r, color.rgb.g, color.rgb.b])  # append to rgb_colors colors after formatted

print(rgb_colors)

img = Image.open('image.jpg')
color_from_pixel = img.getpixel((100, 100))  # other way - extract color from specific pixel
print(color_from_pixel)
