from django.shortcuts import render
from .models import Designer

# Create your views here.
def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})

def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    return render(request, 'detail.heml', {'designer' : designer})
    