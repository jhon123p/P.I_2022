from django.shortcuts import render , HttpResponse , redirect
from app.models import questEconomico


# Create your views here.
def resultado(request):
    
    if request.method == "POST":
        modalidade = request.POST.get('modalidade')
        nome_estudante = request.POST.get('nome_estudante')
        matricula = request.POST.get('matricula')
        genero = request.POST.get('genero')
        data_nascimento = request.POST.get('data_nascimento')
        curso = request.POST.get('curso')
        Identidade = request.POST.get('Identidade')
        renumeracao = request.POST.get('renumeracao')
        nome_Completo = request.POST.get('nome_Completo')
        cpf = request.POST.get('cpf')
        Data_Nascimento = request.POST.get('Data_Nascimento')
        endereco = request.POST.get('endereco')
        nrTelCelular = request.POST.get('nrTelCelular')
        ##arquivo.save()
        questEconomico.objects.create(modalidade = modalidade,
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

def cadastro(request):
    return render(request , 'teste_inscricao.html')