def plotMood(moodData, email, year, savePath):
	from datetime import timedelta, date	
	import math
	import matplotlib.pyplot as plt
	from mpl_toolkits.axes_grid1 import make_axes_locatable
	import numpy as np
	
	# Get rows corresponding to the right year
	moodDataForYear = [];
	for ii in moodData:
		if date(year = year, month = 1, day = 1) <= ii[0] <= date(year = year, month = 12, day = 31):
			moodDataForYear.append(ii)
			
	# Do the plotting
	monthTransitions = []
	dateToPlot = date(year = year, month = 1, day = 1)
	dateNumber = 1
	moodGrid = np.empty((53,7))
	moodGrid[:] = np.NaN
	initialShift = dateToPlot.weekday()
	
	if initialShift == 7:
		initialShift = 0	
	while dateToPlot <= date(year = year, month = 12, day = 31):
	
		
		# Determine the x coordinate
		weekday = dateToPlot.weekday()
		weekday += 1
		if weekday == 7:
			weekday = 0			
		x = weekday
	    
	    # Determine the y coordinate
		y = math.floor((dateNumber+initialShift)/7)
		
		# Grab mood rating
		for ii in moodDataForYear:
			if ii[0] == dateToPlot:
				moodRating = ii[1]				
		moodGrid[y,x] = moodRating
		moodRating = np.NaN
		
		# Check if month transition
		currentMonth = dateToPlot.month
		tomorrowsDate = dateToPlot + timedelta(days=1)
		tomorrowsMonth = tomorrowsDate.month
		if int(tomorrowsMonth - currentMonth) == 1:
			monthTransitions.append([x,y])
		
		
		# iterate to the next day
		one_day = timedelta(days=1)
		dateToPlot += one_day
		dateNumber += 1
		
		if dateToPlot == date(year = year, month = 12, day = 31):
			monthTransitions.append([x+1,y])
		
	
	plt.figure()
	ax = plt.gca()
	
	for ii in monthTransitions:
		x=ii[0]
		y=ii[1]
		lineWidthValue = 0.75
		plt.plot([x+0.5, x+0.5], [y-0.5,y+0.5], color='black', linewidth=lineWidthValue)
		plt.plot([-0.5, x+0.5], [y+0.5,y+0.5], color='black', linewidth=lineWidthValue)
		plt.plot([x+0.5, 6.5], [y-0.5,y-0.5], color='black', linewidth=lineWidthValue)
		
	plt.plot([initialShift+0.5, initialShift+0.5], [-0.5, 0.5 ], color='black', linewidth=lineWidthValue)
	plt.plot([-0.5, initialShift+0.5], [0.5, 0.5], color='black', linewidth=lineWidthValue)
	plt.plot([initialShift+0.5, 6.5], [-0.5, -0.5], color='black', linewidth=lineWidthValue)
	plt.plot([-0.5])
	plt.plot([-0.5, -0.5], [0.5, 52.5], color='black', linewidth=lineWidthValue)
	plt.plot([6.5, 6.5], [-0.5, 51.5], color='black', linewidth=lineWidthValue)
	

	plt.xlim([-0.6, 6.6])
	plt.ylim([52.6, -0.6])
	
	plt.axis('off')
	#plt.xticks([0,1,2,3,4,5,6], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat'], rotation=30)
	
	fontSizeValue=5
	rotationValue=90
	yLegendValue=-1
	xLegendValue = -0.9
	plt.text(-0.5, yLegendValue, 'Sun', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')
	plt.text(-0.5+1, yLegendValue, 'Mon', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')
	plt.text(-0.5+2, yLegendValue, 'Tue', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')
	plt.text(-0.5+3, yLegendValue, 'Wed', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')
	plt.text(-0.5+4, yLegendValue, 'Thu', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')
	plt.text(-0.5+5, yLegendValue, 'Fri', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')
	plt.text(-0.5+6, yLegendValue, 'Sat', rotation=rotationValue, fontsize=fontSizeValue, horizontalalignment='left', verticalalignment='bottom')


	plt.text(xLegendValue, 2.5, 'Jan', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[0][1]+monthTransitions[1][1])/2+1, 'Feb', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[1][1]+monthTransitions[2][1])/2+1, 'Mar', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[2][1]+monthTransitions[3][1])/2+1, 'Apr', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[3][1]+monthTransitions[4][1])/2+1, 'May', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[4][1]+monthTransitions[5][1])/2+1, 'Jun', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[5][1]+monthTransitions[6][1])/2+1, 'Jul', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[6][1]+monthTransitions[7][1])/2+1, 'Aug', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[7][1]+monthTransitions[8][1])/2+1, 'Sep', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[8][1]+monthTransitions[9][1])/2+1, 'Oct', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[9][1]+monthTransitions[10][1])/2+1, 'Nov', fontsize=fontSizeValue, horizontalalignment='right')
	plt.text(xLegendValue, (monthTransitions[10][1]+monthTransitions[11][1])/2+1, 'Dec', fontsize=fontSizeValue, horizontalalignment='right')



	im = plt.imshow(moodGrid)
	#plt.colorbar(location='bottom', shrink=.5, pad=.2, aspect=10)
	divider = make_axes_locatable(ax)
	cax = divider.append_axes("bottom", size="1%", pad=0.05)
   
	cbar = plt.colorbar(im, cax=cax, orientation='horizontal')
	minRating = np.nanmin(moodGrid)
	maxRating = np.nanmax(moodGrid)
	colorBarTicks = np.linspace(np.floor(minRating), np.ceil(maxRating), int(np.ceil(maxRating)) - int(np.floor(minRating)) + 1 )
	cbar.set_ticks(colorBarTicks)
	cbar.ax.tick_params(labelsize=fontSizeValue) 
	plt.savefig("{}/{}_{}.png".format(savePath, email, year), dpi=1000, bbox_inches='tight')

	#plt.show() 
	
		
