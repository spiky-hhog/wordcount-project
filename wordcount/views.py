from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{"Lukasz": "Malkiewicz"})

def about(request):
    return render(request,'about.html')

def eggs(request):
    return HttpResponse('<h1>Hello Lukie-Eggs!</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    count = len(wordlist)
    histogram = {}

    for word in wordlist:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1


    print(histogram)
    sortedhist = sorted(histogram.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':count, 'histogram':sortedhist})
