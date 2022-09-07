def compare(moodData, comparisonAKeyWords, comparisonBKeyWords):

# B trumps A -- if A contains "exercise" and B contains "not exercise", the rating for "did not exercise" will end up in B

    import seaborn
    import matplotlib as plt

    comparisonAComments = []
    comparisonARatings = []
    comparisonBComments = []
    comparisonBRatings = []

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
            comparisonARatings.append(ii[1])
            comparisonAComments.append(ii[2])
        if trueForB == 1:
            # go in B
            comparisonBRatings.append(ii[1])
            comparisonBComments.append(ii[2])
        if trueForA == 0 and trueForB == 0 and 'REMAINDER' in comparisonBKeyWords:
            # go in B
            comparisonBRatings.append(ii[1])
            comparisonBComments.append(ii[2])

    ax = seaborn.violinplot(data=[comparisonARatings, comparisonBRatings], inner=None, color=".8")
    ax = seaborn.stripplot(data=[comparisonARatings, comparisonBRatings], edgecolor="black",alpha=.3, s=15,linewidth=1.0)
    ax.set_xticklabels(['A', 'B'])
    ax.set_ylabel('Mood Rating')

    plt.pyplot.show()
    plt.savefig('custom.png')

    print('dumb')