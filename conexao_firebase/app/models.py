from django.db import models


# Create your models here.
class questEconomico(models.Model):
    modalidade = models.CharField(max_length = 20)
    nome_estudante = models.CharField(max_length = 20)
    matricula = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 20)
    data_nascimento = models.DateTimeField(verbose_name = "Data_nascimento")
    curso = models.CharField(max_length = 20)
    Identidade = models.CharField(max_length = 10)
    renumeracao = models.CharField(max_length = 20)
    ## Informaçoes Basicas
    nome_Completo = models.CharField(max_length = 20)
    cpf = models.CharField(max_length = 20)
    Data_Nascimento = models.DateField(verbose_name = 'Data_nascimento')
    endereco = models.CharField(max_length = 20)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')



def __str__(self):
    return self.nome_completo



#class SettingsForm(forms.ModelForm):
  #  receive_newsletter = forms.BooleanField()

   # class Meta:
    #    model = Settings
