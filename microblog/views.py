from django.shortcuts import render, get_object_or_404
from microblog.models import Post, Categoria
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError, get_connection
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import ListView

def index(request):
    categorias = Categoria.objects.all()
    latest = Post.objects.order_by('-id')[0]

    #Paginação
    post_list = Post.objects.order_by('-id')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'categorias': categorias,
        'posts': posts,
        'latest': latest
    }

    return render(request, 'microblog/home.html', context)

def ver_post(request, url):
    categorias = Categoria.objects.all()
    post = get_object_or_404(Post, url=url)

    context = {
        'post': post,
        'categorias': categorias
    }

    return render(request, 'microblog/ver_post.html', context)

def ver_categoria(request, url):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, url=url)
    latest = Post.objects.filter(categoria=categoria).order_by('-id')[0]

    #Paginação
    post_list = Post.objects.filter(categoria=categoria).order_by('-id')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'titulo': categoria.titulo,
        'posts': posts,
        'categorias': categorias,
        'latest': latest
    }

    return render(request, 'microblog/ver_categoria.html', context)

def ver_usuario(request, pk):
    categorias = Categoria.objects.all()
    usuario = get_object_or_404(User, id=pk)
    latest = Post.objects.filter(autor=usuario.id).order_by('-id')[0]

    #Paginação
    post_list = Post.objects.filter(autor=usuario.id).order_by('-id')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'usuario': usuario,
        'posts': posts,
        'categorias': categorias,
        'latest': latest
    }

    return render(request, 'microblog/ver_usuario.html', context)

def sobre(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, 'microblog/sobre.html', context)

def contact_view(request):
    submitted = False

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            #Ambiente oficial - Envio de email
            '''
            try:
                #Não permitindo envio de e-mails em ambiente de desenvolvimento com assert False
                #assert False
                send_mail(
                    form.cleaned_data['assunto'],
                    form.cleaned_data['mensagem'],
                    settings.EMAIL_HOST_USER,
                    ['email'],
                    fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            '''

            #Ambiente de testes - Envio de email
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                form.cleaned_data['assunto'],
                form.cleaned_data['mensagem'],
                settings.EMAIL_HOST_USER,
                ['email@email.com'],
                connection=con
            )

            return HttpResponseRedirect('/contato?submitted=True')

    else:
        form = ContactForm()

        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
    }

    return render(request, 'microblog/contato.html', context)

def buscar_resultados(request):
    categorias = Categoria.objects.all()

    #Buscando resultados
    query = request.GET.get('q')

    if query:
        post_list = Post.objects.filter(titulo__icontains=query).order_by('-id')
    else:
        post_list = Post.objects.all()

    #Paginação
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'categorias': categorias,
        'posts': posts,
        'query': query
    }

    return render(request, 'microblog/buscar_resultados.html', context)