from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserFrom
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'User {name}, Age {age}')
    else:
        form = UserFrom()
        return render(request, 'app/index.html',context={'form': form})

def myForm(request):
    return render(request, 'app/MyForm', context={'login': login})

# def user(request):
#     name = request.POST.get('name')
#     age = request.POST.get('age')
#     return HttpResponse(f'User {name}, Age {age}')
