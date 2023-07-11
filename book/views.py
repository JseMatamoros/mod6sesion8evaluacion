from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.views.generic import TemplateView
from .models import Book
from .forms import BookForm, LoginForm
# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'
    
class BookListView(TemplateView):
    template_name = 'book_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        high_rated_books = Book.objects.filter(valoracion__gt=1500)
        context['books'] = books
        context['high_rated_books'] = high_rated_books
        return context
    
class InputBookView(TemplateView):
    template_name = 'input_book.html'
    
    def get(self, request, *args, **kwargs):
        form = BookForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            # procesar los datos del formulario
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            valoracion = form.cleaned_data['valoracion']
            # crear una instancia delmodelo Book con los datos ingresados
            libro = Book(titulo = titulo, autor=autor, valoracion=valoracion)
            libro.save()
            # redireccionar a la pagina de exito
            return render(request, 'success.html')
        else:
            return render(request, self.template_name, {'form': form})
        
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_success')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})
            
def registro_success_view(request):
    return render(request, 'registro_success.html')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario utilizando las credenciales proporcionadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigir a la página de "Listar" después del inicio de sesión
    else:
        form = AuthenticationForm(request)
    return render(request, 'custom_login.html', {'form': form})

def custom_logout(request):
    django_logout(request)  # Realizar el logout a través de Django
    return redirect('index')


