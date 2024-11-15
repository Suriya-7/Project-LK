from django.shortcuts import render


def baseLayout(request):
    return render(request, 'baseContent.html')