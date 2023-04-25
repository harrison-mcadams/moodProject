import getMoodData, plotMood_gettingCrazy, locateDate

# Define the paths
csvPath = '/Users/harrisonmcadams/Desktop'
savePath = '/Users/harrisonmcadams/Desktop'

email='harrison.mcadams@gmail.com'
years=[2021, 2022, 2023]

moodData = getMoodData.getMoodData(email, csvPath)

for year in years:
	plotMood_gettingCrazy.plotMood(moodData, email, year, savePath)
	locateDate.locateDate(moodData, email, year, savePath)

