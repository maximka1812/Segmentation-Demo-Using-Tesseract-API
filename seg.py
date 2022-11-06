from PIL import Image, ImageDraw
from tesserocr import PyTessBaseAPI, RIL, PT, iterate_level, PSM
import sys

print("Tesseract API Page Segmentation Example")

filename = "example1.jpg"

if len(sys.argv) == 1:
		print("You must supply image file name!")
		exit()
else: 
	filename = sys.argv[1]


img = Image.open(filename)

results = []
with PyTessBaseAPI() as api:
	api.SetImage(img)
	api.SetPageSegMode(PSM.AUTO_ONLY)
	iterator = api.AnalyseLayout()
	for w in iterate_level(iterator, RIL.BLOCK):
		if w is not None:
			results.append((w.BlockType(), w.BlockPolygon()))
print('Found {} page segmentation blocks.'.format(len(results)))

draw = ImageDraw.Draw(img)
for block_type, poly in results:
	# Now we use different color per block type (see tesserocr.PT for block types list)
	if block_type==PT.FLOWING_TEXT:
		draw.line(poly + [poly[0]], fill=(0, 255, 0), width=4)
	elif block_type==PT.HEADING_TEXT:	
		draw.line(poly + [poly[0]], fill=(255, 0, 0), width=4)
	elif block_type in {PT.FLOWING_IMAGE, PT.PULLOUT_IMAGE, PT.HEADING_IMAGE}:	
		draw.line(poly + [poly[0]], fill=(0, 0, 255), width=4)
	else: 	
		draw.line(poly + [poly[0]], fill=(0, 255, 255), width=4)

#Show image

img.show()