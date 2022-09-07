def moodModel(moodData, positiveKeywords, negativeKeywords, analysisTypes):
    import numpy as np


    for xx in range(0, len(positiveKeywords)):


        xVector = []

        comparisonAKeyWords = positiveKeywords[xx]
        comparisonBKeyWords = negativeKeywords[xx]
        for ii in moodData:
            trueForA = 0
            trueForB = 0
            for aa in comparisonAKeyWords:
                if aa.lower() in ii[2].lower():
                    trueForA = 1
            for bb in comparisonBKeyWords:
                if bb.lower() in ii[2].lower():
                    trueForB = 1
            if trueForA == 1 and trueForB == 0:
                # go in A
                xVector.append(analysisTypes[xx][0])
            if trueForB == 1:
                # go in B
                xVector.append(analysisTypes[xx][1])
            if trueForA == 0 and trueForB == 0 and 'REMAINDER' in comparisonBKeyWords:
                # go in B
                xVector.append(analysisTypes[xx][1])
            if trueForA == 0 and trueForB == 0 and 'REMAINDER' in comparisonAKeyWords:
                # go in B
                xVector.append(analysisTypes[xx][0])
        xArray = np.array(xVector).reshape((-1, 1))
        if xx == 0:
            x = np.array(xArray)
        if xx > 0:
            x = np.stack((x, xArray))
        print(xVector)

    if len(positiveKeywords) > 1:
        x = np.rot90(x, -1)
        x = np.fliplr(x)

    y = []
    for ii in moodData:
        y.append(ii[1])

    y = np.array(y)

    print(x)
    print(y)

    from sklearn.linear_model import LinearRegression

    nanValues = np.argwhere(np.isnan(y))

    for ii in nanValues:
        x = np.delete(x, ii, axis=0)
        y = np.delete(y, ii)

    model = LinearRegression()
    model.fit(x, y)

    print(model.coef_)

