def getMoodData(email, csvPath):

	import csv
	file = open("{}/{}_MoodRatings.csv".format(csvPath, email))
	csvreader = csv.reader(file, delimiter='\t')
	header = next(csvreader)

	rows = []
	import numpy
	for row in csvreader:

		if not(row[0]):
			print('dumb')
		else:

			rows.append(row)



	from datetime import datetime, date
	import calendar

	dates = []
	moodData = [];
	for row in rows:
		# print(row)
		monthNumber = list(calendar.month_abbr).index(row[1])
		# print(month_number)

		dateNum = date(year=int(row[0]), month=monthNumber, day=int(row[2]))

		if len(row[4]) != 0:
			moodRating = float(row[4])
		else:
			moodRating = numpy.nan
		comments = row[5]
		# print(dateNum)
		dates.append(dateNum)

		moodData.append([dateNum, moodRating, comments])

	moodData.sort()
	


	return moodData
	
#difference = (dates[0] - dates[1])
#print(difference.days)
	
	