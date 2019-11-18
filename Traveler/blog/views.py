from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'blog/Index.html', {})

def RegistroUsuario(request):
    return render(request, 'blog/RegistroUsuario.html', {})

