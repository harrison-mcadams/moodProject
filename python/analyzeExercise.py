import compare, getMoodData

email='harrison.mcadams@gmail.com'
year=2020
csvPath = '/var/www/html/login'

moodData = getMoodData.getMoodData(email, csvPath)

comparisonAKeyWords = ['exercise', 'worked out', 'working out', 'work out', 'workout', 'run', 'yoga', 'madfit', 'abs']
comparisonBKeyWords = ['not working out', 'not work out', 'no exercise', 'not exercise', 'REMAINDER']

compare.compare(moodData, comparisonAKeyWords, comparisonBKeyWords)