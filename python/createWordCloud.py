def createWordCloud(moodData, email, savePath):

    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, STOPWORDS
    import makeWebpages

    stopwords = set(STOPWORDS)
    stopwords.add('day')
    stopwords.add('got')
    stopwords.remove('not')
    stopwords.remove('didn\'t')

    comments = ''
    for i in moodData:
        newComment = i[2]
        comments = comments + ' ' + newComment
    w = 800
    h = 800
    wordcloud = WordCloud(width=w, height=h,
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

    #plt.show()
    plt.savefig("{}/{}_wordCloud.png".format(savePath, email), dpi=1000, bbox_inches='tight')

    f = open("{}/{}_wordCloud.php".format(savePath, email), 'w')
    location = 'post-signin'
    f = makeWebpages.makeHeader(f, email, location)
    f.write(
        "      <img src='{}/{}_wordCloud.png' alt='My test image' usemap='#workmap' width='{}' height='{}'>\n".format(savePath, email,
                                                                                                            w, h))
    f.write("</html>\n")
    f.close()

