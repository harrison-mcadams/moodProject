def locateDate(moodData, email, year)

#email = 'harrison.mcadams@gmail.com'
#year = 2021

	import numpy as np
	import cv2
	from scipy.signal import find_peaks
	from matplotlib import pyplot as plt
	from datetime import timedelta, date	

	pathToImage='/Users/harrisonmcadams/Desktop'

	fullImagePath='{}/{}_{}.png'.format(pathToImage, email, year)

	from PIL import Image
	from collections import Counter

	# Separate RGB arrays
	im = Image.open(fullImagePath)
	R, G, B = im.convert('RGB').split()
	r = R.load()
	g = G.load()
	b = B.load()
	w, h = im.size
	print('image size:', w, h)

	# Convert non-black pixels to white
	for i in range(w):
		for j in range(h):
			if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
				r[i, j] = 255 # Just change R channel

	# Merge just the R channel as all channels
	im = Image.merge('RGB', (R, R, R))
	im.save("{}/black_and_white.png".format(pathToImage))



	image = cv2.imread("{}/black_and_white.png".format(pathToImage))
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Set threshold level
	threshold_level = 50

	# Find coordinates of all pixels below threshold
	coords = np.column_stack(np.where(gray < threshold_level))

	x=[]
	y=[]
	for ii in coords:
		x.append(ii[1])
		y.append(ii[0])
		#print(x)


	c = Counter(x)
	mostCommon=c.most_common(20)
	sortedMostCommon = (sorted(mostCommon))

	sortedMostCommonXs = []
	sortedMostCommonYs = []


	for ii in sortedMostCommon:
		sortedMostCommonXs.append(ii[0])
		sortedMostCommonYs.append(ii[1])
	
	print(sortedMostCommonXs)


	def gaussian( x , s):
		return 1./np.sqrt( 2. * np.pi * s**2 ) * np.exp( -x**2 / ( 2. * s**2 ) )

	fullXRange = list(range(sortedMostCommonXs[0]-10, sortedMostCommonXs[len(sortedMostCommonXs)-1]+10))

	myGaussian = np.fromiter( (gaussian( x , 10 ) for x in range( 0, len(sortedMostCommonXs), 1 ) ), np.float )
	#filterdData = gaussian_filter1d( myData, 1 )

	myData = []
	foundMatch = 0
	for ii in fullXRange:
		myData.append(0)
		for jj in range(0, len(sortedMostCommonXs), 1):
			if ii == sortedMostCommonXs[jj]:
				myData.append(sortedMostCommonYs[jj])
				foundMatch = 1

			

	print(myData)
			

	myFilteredData = np.convolve( myData, myGaussian,'valid')
	print(myFilteredData)

	# To debug the convolution
	fig = plt.figure(1)
	ax = fig.add_subplot( 2, 1, 1 )
	ax.plot( myData, marker='x', label='peak' )
	ax.plot( myGaussian, marker='^',label='filter1D smeared peak' )
	ax.plot( myGaussian, marker='v',label='test Gaussian' )
	ax.plot( myFilteredData, marker='v', linestyle=':' ,label='convolve smeared peak' )
	ax.legend( bbox_to_anchor=( 1.05, 1 ), loc=2 )	


	peaks = find_peaks(myFilteredData, height = 1, threshold = 1, distance = 100)
	height = peaks[1]['peak_heights'] #list of the heights of the peaks
	#peak_pos = fullXRange[peaks[0]] #list of the peaks positions
	print("length of convolved data: ", len(myFilteredData))
	print("length of kernel: ", len(myGaussian))
	print("length of x-range: ", len(fullXRange))
	pixelFudgeFactor = 3
	leftXPixel = fullXRange[peaks[0][0]]+pixelFudgeFactor
	rightXPixel = fullXRange[peaks[0][1]]-pixelFudgeFactor
	print(leftXPixel, rightXPixel)

	# Find the pixel along the right pixel border that's highest up
	yPixelValuesAlongRightBorder = []
	for ii in coords:
		if ii[1] == rightXPixel:
			yPixelValuesAlongRightBorder.append(ii[0])

	upperRightPixelY = (min(yPixelValuesAlongRightBorder))+pixelFudgeFactor

	# Find the left-most pixel along the top border
	xPixelValuesAlongTopBorder = []
	for ii in coords:
		if ii[0] == upperRightPixelY:
			xPixelValuesAlongTopBorder.append(ii[1])

	upperLeftPixelX = min(xPixelValuesAlongTopBorder)+pixelFudgeFactor
	print(upperLeftPixelX)

	boxWidth = round((rightXPixel-leftXPixel)/7)

	# Make some boxes
	dateToPlot = date(year = year, month = 1, day = 1)

	verticalFudgeFactor = 16
	horizontalFudgeFactor = 26
	xCoordinate = upperLeftPixelX+horizontalFudgeFactor
	yCoordinate = upperRightPixelY+verticalFudgeFactor

	f = open("/Users/harrisonmcadams/Desktop/{}_{}.html".format(email,year), 'w')
	f.write("<!DOCTYPE html>\n")

	f.write("<html>\n")
	f.write("  <head>\n")
	f.write("    <meta charset='utf-8'>\n")
	f.write("    <title>Harry 2021</title>\n")
	f.write("    <style> img {\n")
	f.write("float: left;\n")
	f.write("margin: 0px 0px;\n")
	f.write("vertical-align: top;\n")
	f.write("horizontal-align: left;\n")
	f.write("display: inline-block}\n")
	f.write("    </style>\n")
	f.write("  </head>\n")
	f.write("  <body>\n")
	f.write("      <img src='{}_{}.png' alt='My test image' usemap='#workmap' width='874' height='4225'>\n".format(email,year))
	f.write("    </body>\n")
	f.write("    <map name='workmap'>\n")




	while dateToPlot <= date(year = year, month = 12, day = 31):
		rectangleSpecification = [xCoordinate, yCoordinate, xCoordinate+boxWidth, yCoordinate+boxWidth-0.35]
		lst_str = str(rectangleSpecification)[1:-1] 	
		f.write("	    <area shape='rect' coords='{}' alt='Computer' href='{}'>\n".format(lst_str, dateToPlot))
		print(rectangleSpecification)
		xCoordinate = xCoordinate + boxWidth
		if xCoordinate + boxWidth >= rightXPixel+horizontalFudgeFactor:
			xCoordinate = leftXPixel+horizontalFudgeFactor
			yCoordinate = yCoordinate+boxWidth-0.35
	

		one_day = timedelta(days=1)
		dateToPlot += one_day
	
	f.write("  </map>\n")
	f.write("</html>\n")
	f.close()

	
