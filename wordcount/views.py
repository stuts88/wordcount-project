from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.GET['fulltext']
    fulltext_list = fulltext.split()
    length = len(fulltext_list)
    word_count = {}
    for word in fulltext_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1


    sortedWords = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'length':length, 'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')
