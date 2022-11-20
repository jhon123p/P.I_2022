from django.shortcuts import render , HttpResponse , redirect
from app.models import questEconomico


# Create your views here.
def resultado(request):
    
    if request.method == "POST":
        tipo_bolsa = request.POST.get('tipo_bolsa')
        nome_completo = request.POST.get('nome_completo')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        nrTelCelular = request.POST.get('nrTelCelular')
        arquivo = request.FILES["arquivo"]
        ##arquivo.save()
        questEconomico.objects.create(tipo_bolsa = tipo_bolsa,
                                      nome_completo = nome_completo,
                                      data_nascimento = data_nascimento,
                                      cpf = cpf,
                                      endereco = endereco,
                                      nrTelCelular = nrTelCelular,
                                      arquivo = arquivo)
        return HttpResponse('ARQUIVO ENVIANDO COM SUCESSO')

    return redirect('/resultados')




# Imaginary function to handle an uploaded file.

##import pyrebase 
  

def socio2(request):
    return render(request , 'indice.html')