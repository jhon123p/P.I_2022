from django.db import models


# Create your models here.
class questEconomico(models.Model):
    tipo_bolsa = models.CharField(max_length=20)
    nome_completo = models.CharField(max_length = 50)
    data_nascimento = models.DateTimeField(verbose_name = 'Data nascimento')
    cpf = models.CharField(max_length=11, blank=True, null=True)
    endereco = models.CharField(max_length = 100)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    ##usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    arquivo = models.FileField(upload_to='resultados/')#upload_to='meusarquivos/'

def __str__(self):
    return self.nome_completo



#class SettingsForm(forms.ModelForm):
  #  receive_newsletter = forms.BooleanField()

   # class Meta:
    #    model = Settings
