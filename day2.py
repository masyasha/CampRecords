from PIL import Image, ImageOps

print("Hey there! Welcome to Insta Filters.\n\n\
	Please write the name of your picture: ")
name = input("\t\t\t\t\t      ")

im = Image.open(name).convert('RGBA')
pixels = im.load()

width = im.width
height  = im.height

def make_linear_ramp(white):
    # putpalette expects [r,g,b,r,g,b,...]
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i//255, g*i//255, b*i//255))
    return ramp

print("\nNow make yourself choose a filter, please: \n\
1. Sepia \
2. Schbenjd \
3. Inverse colors \
4. Negative \
5. Snhdijfjd (incoming)")
choice = input("Write a number (1-4): ")


if choice == "1":

	# make sepia ramp (tweak color as necessary)
	sepia = make_linear_ramp((255, 240, 192))


	# convert to grayscale
	if im.mode != "L":
	    im = im.convert("L")

	# optional: apply contrast enhancement here, e.g.
	im = ImageOps.autocontrast(im)

	# apply sepia palette
	im.putpalette(sepia)

	# convert back to RGB so we can save it as JPEG
	# (alternatively, save it in PNG or similar)
	im = im.convert("RGB")


im.show()
# im.save('image.jpg')
