import getMoodData, plotMood

# Define the paths
csvPath = '/Users/harrisonmcadams/Desktop'
savePath = '/Users/harrisonmcadams/Desktop'

email='harrison.mcadams@gmail.com'
years=[2020, 2021]

moodData = getMoodData.getMoodData(email, csvPath)

for year in years:
	plotMood.plotMood(moodData, email, year, savePath)

