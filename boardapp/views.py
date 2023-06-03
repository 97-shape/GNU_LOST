from django.shortcuts import render

# Create your views here.
def guide(request):
    return render(request, "guide.html")

def qna(request):
    return render(request, "QNA.html")

def ask(request):
    return render(request, "ask.html")