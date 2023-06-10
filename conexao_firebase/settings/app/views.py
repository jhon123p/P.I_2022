from django.shortcuts import render , HttpResponse , redirect
from app.models import questSEconomico
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def resultado(request):
    
    if request.method == "POST":
        modalidade = request.POST.get('modalidade')
        nome_estudante = request.POST.get('nome_estudante')
        matricula = request.POST.get('matricula')
        genero = request.POST.get('genero')
        data_nascimento1 = request.POST.get('data_nascimento1')
        curso = request.POST.get('curso')
        Identidade = request.POST.get('Identidade')
        renumeracao = request.POST.get('renumeracao')
        nome_Completo = request.POST.get('nome_Completo')
        cpf = request.POST.get('cpf')
        Data_Nascimento = request.POST.get('Data_Nascimento')
        endereco = request.POST.get('endereco')
        nrTelCelular = request.POST.get('nrTelCelular')
        status = request.POST.get('Status')
        ##arquivo.save()
        questSEconomico.objects.create(modalidade = modalidade,
                                      nome_estudante = nome_estudante ,
                                      matricula = matricula ,
                                      genero = genero ,
                                      data_nascimento1 = data_nascimento1 ,
                                      curso = curso ,
                                      Identidade = Identidade ,
                                      renumeracao = renumeracao ,
                                      nome_Completo = nome_Completo ,
                                      cpf = cpf ,
                                      Data_Nascimento = Data_Nascimento ,
                                      endereco = endereco ,
                                      nrTelCelular = nrTelCelular,
                                      status = status)
                                      
        return render(request, 'home.html')

        #return render()

    return redirect('/home')

# Imaginary function to handle an uploaded file.

##import pyrebase 
@login_required
def inscricoes(request):
    return render(request , 'teste_inscricao.html')
@login_required
def questSo(request):
    return render(request , 'teste.html')

def index(request):
    return render(request , 'registration/login.html')  
    
@login_required
def cadastro(request):
    return render(request , 'inscricoes.html')

@login_required
def home(request):
    return render(request,'home.html')



#def login_(request):
#    if request.method =='POST':
#        usuario = request.POST['usuario']
#        senha = request.POST['senha']
#        user = authenticate(request, username = usuario, password = senha)
#        if user is not None:
#            login(request, user)
#            return redirect('home')
#        else:
#            return redirect('index')#
            
#@login_required
#def logout_(request):
 #   logout(request)
 #   return redirect('index')