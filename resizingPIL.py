from PIL import Image

imageFile = '/Users/Work/Desktop/testsymbol2.png'
im1 = Image.open(imageFile)

im1.thumbnail((500,500), Image.ANTIALIAS)


ext= '.png'
im1.save('Resized2' + ext)
