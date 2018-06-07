

from django.http import HttpResponse
from django.shortcuts import render # this is used for getting attached html file
import operator

def Homepage(request):
        return render(request,'home.html')# this is return html page and we can also pass python code here which is written on html file or as variable
def aboutpage(request):
        return render(request,'about.html')

def birds(request):
        return HttpResponse('This is the bird page')

#def animals(request):
        return HttpResponse('This is the Specfic animal page')

def countfunction (request):
    fulltext=request.GET['fulltext']# BY THIS WE ARE GETTING THE WORDS WRITTEN IN TEXT BOX

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:

        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
        #add to the dictiionary
            worddictionary[word] =1
        sortedwords =  sorted(worddictionary.items(), key= operator.itemgetter(1), reverse= True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
