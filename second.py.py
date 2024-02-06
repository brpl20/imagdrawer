# Second 

from PIL import Image, ImageDraw, ImageFont

# Define the width and height of the image
width, height = 500, 200

# Create a new image with white background
img = Image.new('RGB', (width, height), 'white')

# Create a draw object
draw = ImageDraw.Draw(img)

# Draw a rounded rectangle
rect_x, rect_y, rect_width, rect_height = 50, 50, 400, 100
draw.rounded_rectangle([rect_x, rect_y, rect_x + rect_width, rect_y + rect_height], radius=20, fill='yellow')

# Specify the text and properties
text = "TEXTO"
font = ImageFont.truetype("GothamMedium.ttf", 40)  # You may need to change the font path
textwidth, textheight = draw.textsize(text, font=font)
text_x = rect_x + (rect_width - textwidth) / 2
text_y = rect_y + (rect_height - textheight) / 2

# Add the text to the image
draw.text((text_x, text_y), text, fill='green', font=font)

# Save the image
img.save('banner.png')