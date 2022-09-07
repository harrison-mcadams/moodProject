def createWordCloud(moodData, savePath):

    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, STOPWORDS

    stopwords = set(STOPWORDS)
    stopwords.add('day')
    stopwords.add('got')

    comments = ''
    for i in moodData:
        newComment = i[2]
        comments = comments + ' ' + newComment

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          collocations=True,
                          min_font_size=10).generate(comments)

    def black_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        return ("hsl(0,100%, 1%)")
    wordcloud.recolor(color_func=black_color_func)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
