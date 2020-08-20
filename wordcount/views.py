from django.shortcuts import render
import operator


def home(request):
    return render(request, 'wordcount/home.html')


def count(request):
    fulltext = request.GET['fulltext']

    words = fulltext.split()

    wordcount = {}

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    sortedwords = sorted(
        wordcount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordcount/count.html', {'fulltext': fulltext, 'count': len(words), 'sortedwords': sortedwords})
