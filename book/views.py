from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.views.generic import TemplateView
from .models import Book
from .forms import BookForm
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
            Book.save()
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