from PIL import Image, ImageDraw, ImageFont

# Open the image file
img = Image.open('test.png')
width, height = img.size

# Create a draw object
draw = ImageDraw.Draw(img)

# Specify the text and properties
text = "Pedágio 100% RPPS Paraná\n Art. 5 \n57/60 idade \n30/35 contribuição \n20 Anos Efetivo Exercício Público\n 5  Anos Cargo Efetivo Your Text Here"
#text = "Pedágio 100% RPPS Paraná\n Art. 5 \n57/60 idade \n30/35 contribuição \n20 Anos Efetivo Exercício Público\n 5  Anos Cargo Efetivo Your Text Here"

# You may need to change the font path
textwidth, textheight = draw.textsize(text)
color = 'rgb(0, 0, 0)'  # black color
#font = PIL.ImageFont.truetype(font="B612-Regular.ttf", size=10, index=0, encoding='', layout_engine=None)
#font = ImageFont.truetype(font="/B612-Regular.ttf", size=15)
draw.font = ImageFont.truetype("GothamMedium.ttf", 20)
# Calculate the position of the text (center of the image)
position = ((width-textwidth)/2, (height-textheight)/2)

# Add the text to the image
draw.text(position, text, fill=color)

# Save the image
img.save('text_image.png')
