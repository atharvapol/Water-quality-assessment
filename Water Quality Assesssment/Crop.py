from PIL import Image

img = Image.open('8_sur_org.png')

img = img.crop((610,336,1173,948))

img.save('8_sur_new.png')
