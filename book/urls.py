from django.urls import path
from .views import IndexPageView, BookListView, InputBookView, registro_view, registro_success_view
from . import views

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('listbook/', BookListView.as_view(), name='listbook'),
    path('inputbook/', InputBookView.as_view(), name='input_book'),
    path('registro/', registro_view, name='registro'),
    path('registro/success/', registro_success_view, name='registro_success'),
    path('custom_login/', views.custom_login, name='custom_login'),    
    path('logout/', views.custom_logout, name='logout'),
]