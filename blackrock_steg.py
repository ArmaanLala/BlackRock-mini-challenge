from PIL import Image

im = Image.open('imageEmbedded.png')
pix = im.load()
width, height = im.size
for x in range(0, width):
    for y in range(0, height):
        r, g, b = pix[x, y]
        if (r, g, b) == (0, 0, 0):
            pix[x, y] = (34, 189, 239)
        else:
            pix[x,y] = (0,0,0)
im.save('Decrypted.png')
