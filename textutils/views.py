from django.http import HttpResponse
from django.shortcuts import render

def home(request):
#   params ={'name':'gyanendra','class':'7'}
#   this is the way of sending variables into template
  return render(request,'index.html')


def analyze(request):
     # request.GET.get returns the text whatever will be in tags otherwise 
    # default valuewill come,here we are getting the text
    djtext= print(request.GET.get('text','default'))
    # print(djtext)
#    here we are analysing the text
# get the text
    djtext = request.GET.get('text', 'default')
# check the checkbox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')


# check which chekbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            djtext = analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext = analyzed
        
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!='\r':
               analyzed=analyzed+char
            else:
                analyzed=analyzed+" "
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in  enumerate(djtext):
            if (djtext[index]==' ' or djtext[index]=='\n') and (djtext[index+1]==' ' or djtext[index+1]=='\n'):
               continue
            else:
               analyzed=analyzed+char
        djtext = analyzed
     

    if(charcount=="on"):
        c=0
        for char in djtext:
          c =c+1 
          params = {'purpose': 'char is counted', 'analyzed_text': analyzed+"\n character count is "+str(c)}
        return render(request, 'analyze.html', params)
    else:
        params = {'purpose': '', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

