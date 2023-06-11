from django.shortcuts import render

# Create your views here.
def index(request):
    print("Recibiendo petición en la ruta index")
    context = {
        "name": "Kate",
        "website":  {
            "name": "Loop Marketplace",
            "author": "Jhon Doe"
        },
        "numbers": [2, 4, 8, 10, 12]
    }
    return render(request, 'index.html', context = context)