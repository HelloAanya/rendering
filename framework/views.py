from django.shortcuts import render

def index(request):
    context = {
        # You can add more context variables here if needed
    }
    return render(request, 'index.html', context)


