from aplicaciones.Usuario.views import LoginView, RegisterView, LogOut, UsuarioUpdate, Principal
from django.urls import path


urlpatterns = [
    path('', Principal, name="principal"),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='registrar'),
    path('logout', LogOut, name='logout'),
    path('actualizar/<int:pk>/', UsuarioUpdate.as_view(), name='actualizar'),


]
