from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {
        'heading': 'Welcome to Django',
        'paragraph': 'Django is high level web framework for perfectionist with deadlines.'
    }
    return render(request, 'item/index.html', context=dict)
