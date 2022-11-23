from django.contrib import admin

# Register your models here.
from app.models import questSEconomico

class display(admin.ModelAdmin):
    list_display = ('modalidade' , ) #metodo de mostrar dados em display
    list_filter = ('cpf',)

admin.site.register(questSEconomico , display)