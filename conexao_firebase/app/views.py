from django.shortcuts import render , HttpResponse , redirect
from app.models import questSEconomico
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def resultado(request):
    
    if request.method == "POST":
        modalidade = request.POST.get('modalidade')
        nome_estudante = request.POST.get('nome_estudante')
        matricula = request.POST.get('matricula')
        genero = request.POST.get('genero')
        data_nascimento = request.POST.get('data_nascimento1')
        curso = request.POST.get('curso')
        Identidade = request.POST.get('Identidade')
        renumeracao = request.POST.get('renumeracao')
        nome_Completo = request.POST.get('nome_Completo')
        cpf = request.POST.get('cpf')
        Data_Nascimento = request.POST.get('Data_Nascimento')
        endereco = request.POST.get('endereco')
        nrTelCelular = request.POST.get('nrTelCelular')
        ##arquivo.save()
        questSEconomico.objects.create(modalidade = modalidade,
                                      nome_estudante = nome_estudante ,
                                      matricula = matricula ,
                                      genero = genero ,
                                      data_nascimento = data_nascimento ,
                                      curso = curso ,
                                      Identidade = Identidade ,
                                      renumeracao = renumeracao ,
                                      nome_Completo = nome_Completo ,
                                      cpf = cpf ,
                                      Data_Nascimento = Data_Nascimento ,
                                      endereco = endereco ,
                                      nrTelCelular = nrTelCelular)
        return HttpResponse('ARQUIVO ENVIANDO COM SUCESSO')

    return redirect('/resultados')

# Imaginary function to handle an uploaded file.

##import pyrebase 
def index(request):
    return render(request , 'index.html')  
@login_required
def cadastro(request):
    return render(request , 'teste_inscricao.html')
@login_required
def home(request):
    return render(request,'home.html')

def login_(request):
    if request.method =='POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username = usuario, password = senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('index')
@login_required
def logout_(request):
    logout(request)
    return redirect('index')