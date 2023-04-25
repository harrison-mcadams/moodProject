import getMoodData, moodModel

csvPath = '/Users/harrisonmcadams/Desktop'
savePath = '/Users/harrisonmcadams/Desktop'

email='harrison.mcadams@gmail.com'
years=[2020]

moodData = getMoodData.getMoodData(email, csvPath)

positiveExerciseKeywords = ['exercise', 'worked out', 'working out', 'work out', 'workout', 'run', 'yoga', 'madfit', 'abs']
negativeExerciseKeywords = ['not working out', 'not work out', 'no exercise', 'not exercise', 'skipped working out', 'REMAINDER']

positiveProductiveKeywords = ['productive']
negativeProductiveKeywords = ['unproductive', 'not very productive', 'didn\'t feel particularly productive', 'not at all productive', 'wasn\'t able to be productive', 'not really productive']

#positiveKeywords = [['exercise', 'worked out', 'working out', 'work out', 'workout', 'run', 'yoga', 'madfit', 'abs'], ['call']]
#negativeKeywords = [['not working out', 'not work out', 'no exercise', 'not exercise', 'skipped working out', 'REMAINDER'], ['boring']]
#analysisTypes = [[1,0], [1,0]]

#positiveKeywords = [['exercise', 'worked out', 'working out', 'work out', 'workout', 'run', 'yoga', 'madfit']]
#negativeKeywords = [['not working out', 'not work out', 'no exercise', 'not exercise', 'skipped working out', 'REMAINDER']]
#analysisTypes = [[1,0]]

#positiveKeywords = [['productive']]
#negativeKeywords = [['unproductive', 'not very productive', 'didn\'t feel particularly productive', 'not at all productive', 'wasn\'t able to be productive', 'not really productive']]
#analysisTypes = [[1,0]]

#positiveKeywords = [['+g']]
#negativeKeywords = [['REMAINDER']]
#analysisTypes = [[1,0]]

#moodModel.moodModel(moodData, [positiveExerciseKeywords, positiveProductiveKeywords],
#                    [negativeExerciseKeywords, negativeProductiveKeywords],
#                    [[1,0], [1,0]])

moodModel.moodModel(moodData, [positiveExerciseKeywords], [negativeExerciseKeywords], [[1,0]])