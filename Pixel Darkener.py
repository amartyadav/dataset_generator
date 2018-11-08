from PIL import Image
img= Image.open('/Users/Work/Desktop/Resized2.png')
pixels = img.load()


for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i,j] > (0,0,0,255) and pixels[i,j] < (220,220,220,255):
            pixels[i,j] = (0,0,0,255)


ext= '.png'
img.save('DarkResized2' + ext)