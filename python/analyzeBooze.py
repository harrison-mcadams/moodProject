def analyzeBooze(moodData, savePath):

    import re, numpy
    from datetime import datetime, date
    import matplotlib.pyplot as plt

    drinks = []
    dates = []

    priorDate = []
    for ii in moodData:

        comment = ii[2]

        drinkString = re.search(r'\d+ drink', comment)

        if drinkString:
            drinkString = drinkString.group()
            nDrinks = re.findall(r'\d+', drinkString)
            nDrinks = int(nDrinks[0])
            print(nDrinks)
            print(ii[0])
        else:
            nDrinks = numpy.nan


        if priorDate == ii[0]:
            drinks[-1] = nDrinks
            dates[-1] = ii[0]
        else:
            drinks.append(nDrinks)
            dates.append(ii[0])

        priorDate = ii[0]

    startDate = date(2022, 10, 8)
    startIndex = dates.index(startDate)

    #startIndex = 880

    # total drinks this week so far since Monday
    mondays = []
    for dd in dates[startIndex:]:
        if dd.weekday() == 0:
            mondays.append(dd)

    goodDates = []
    goodDrinks = []

    badDates = []
    badDrinks = []

    for mm in mondays:
        mondayIndex = dates.index(mm)
        if mondayIndex + 6 <= len(dates)-1:
            if sum(drinks[mondayIndex:mondayIndex+7]) <= 14:
                goodDates.append(dates[mondayIndex])
                goodDates.append(dates[mondayIndex+1])
                goodDates.append(dates[mondayIndex+2])
                goodDates.append(dates[mondayIndex+3])
                goodDates.append(dates[mondayIndex+4])
                goodDates.append(dates[mondayIndex+5])
                goodDates.append(dates[mondayIndex+6])

                goodDrinks.append(drinks[mondayIndex])
                goodDrinks.append(drinks[mondayIndex + 1])
                goodDrinks.append(drinks[mondayIndex + 2])
                goodDrinks.append(drinks[mondayIndex + 3])
                goodDrinks.append(drinks[mondayIndex + 4])
                goodDrinks.append(drinks[mondayIndex + 5])
                goodDrinks.append(drinks[mondayIndex + 6])
            elif sum(drinks[mondayIndex:mondayIndex+7]) > 14:
                badDates.append(dates[mondayIndex])
                badDates.append(dates[mondayIndex+1])
                badDates.append(dates[mondayIndex+2])
                badDates.append(dates[mondayIndex+3])
                badDates.append(dates[mondayIndex+4])
                badDates.append(dates[mondayIndex+5])
                badDates.append(dates[mondayIndex+6])

                badDrinks.append(drinks[mondayIndex])
                badDrinks.append(drinks[mondayIndex + 1])
                badDrinks.append(drinks[mondayIndex + 2])
                badDrinks.append(drinks[mondayIndex + 3])
                badDrinks.append(drinks[mondayIndex + 4])
                badDrinks.append(drinks[mondayIndex + 5])
                badDrinks.append(drinks[mondayIndex + 6])




    # average number of drinks per day lifetime
    meanDrinks = numpy.nanmean(drinks[startIndex:])
    meanDrinksFormatted = "{:.2f}".format(meanDrinks)


    # lifetime plot
    fig, ax = plt.subplots()
    plt.plot_date(dates[startIndex:], drinks[startIndex:], '--ko')
    plt.plot_date(goodDates, goodDrinks, 'go')
    plt.plot_date(badDates, badDrinks, 'ro')
    ax.xaxis.set_tick_params(rotation=20, labelsize=10)
    ax.set_xticks(mondays)
    plt.gca().set_ylim(bottom=-0.2)
    plt.locator_params(axis="y", integer=True)

    plotTitle = 'Average Number of Drinks per Day = ' + str(meanDrinksFormatted)
    plt.title(plotTitle)

    plt.savefig("{}/lifetime.png".format(savePath), format='png', dpi=1000, bbox_inches='tight')


    # most recent week plot

    drinksThisWeek = sum(drinks[dates.index(mondays[-1]):])
    fig2, ax2 = plt.subplots()
    plt.plot_date(dates[dates.index(mondays[-1]):], drinks[dates.index(mondays[-1]):], '--ko')
    plotTitle = 'Drinks This Week = ' + str(drinksThisWeek)
    plt.title(plotTitle)
    ax2.xaxis.set_tick_params(rotation=20, labelsize=10)
    plt.locator_params(axis="y", integer=True)
    ax.set_xticks(dates[dates.index(mondays[-1]):])
    plt.gca().set_ylim(bottom=-0.2)
    plt.savefig("{}/thisWeek.png".format(savePath), dpi=1000, bbox_inches='tight')
