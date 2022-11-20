from django.contrib import admin

# Register your models here.
from app.models import questEconomico

class display(admin.ModelAdmin):
    list_display = ('nome_completo','cpf' , 'arquivo') #metodo de mostrar dados em display
    list_filter = ('cpf',)

admin.site.register(questEconomico , display)