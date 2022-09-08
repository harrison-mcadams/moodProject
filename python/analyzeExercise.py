import compare, getMoodData

email='harrison.mcadams@gmail.com'
year=2020
csvPath = '/Users/harrisonmcadams/Desktop'
savePath = '/Users/harrisonmcadams/Desktop'

moodData = getMoodData.getMoodData(email, csvPath)

comparisonAKeyWords = ['exercise', 'worked out', 'working out', 'work out', 'workout', 'run', 'yoga', 'madfit', 'abs']
comparisonBKeyWords = ['not working out', 'not work out', 'no exercise', 'not exercise', 'skipped working out', 'REMAINDER']

comparisonAKeyWords = ['productive']
comparisonBKeyWords = ['unproductive', 'not very productive', 'didn\'t feel particularly productive', 'not at all productive', 'wasn\'t able to be productive', 'not really productive']

comparisonAKeyWords = ['call']
comparisonBKeyWords = ['boring']

compare.compare(moodData, comparisonAKeyWords, comparisonBKeyWords)