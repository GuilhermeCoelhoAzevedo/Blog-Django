from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "microblog"

urlpatterns = [
    #GET
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('search/', views.buscar_resultados, name='buscar_resultados'),

    #Novo padrão Python/GET
    #path('categorias/<int:pk>/<slug:slug>', views.ver_categoria, name='categoria_view'),
    path('categorias/<slug:url>', views.ver_categoria, name='categoria_view'),
    path('posts/<slug:url>', views.ver_post, name='ver_post'),
    path('autores/<int:pk>', views.ver_usuario, name='usuario_view'),

    #GET/POST
    path('contato/', views.contact_view, name='contato'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Adicionando caminho de midia para o app

