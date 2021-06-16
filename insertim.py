from PIL import Image, ImageDraw, ImageFilter

def img(x,y,img):
	im1 = Image.open(img)
	im2 = Image.open('star.png')
	img_w, img_h = im2.size
	back_im = im1.copy()
	back_im.paste(im2, (x-int(img_w/2), y-int(img_h/2)),im2)
	back_im.save('paste_pos.jpg', quality=95)