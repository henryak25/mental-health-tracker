from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306214990',
        'name': 'Henry Aditya Kosasi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
