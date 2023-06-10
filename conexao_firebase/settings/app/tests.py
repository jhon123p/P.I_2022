from django.test import TestCase
from .models import questSEconomico
from datetime import datetime
from django.utils.timezone import make_aware
# Create your tests here.

class  TestPaginaInicial(TestCase):


        # Cria uma instância do modelo com dados válidos
        dados_validos = {
            'modalidade': 'Modalidade',
            'nome_estudante': 'Nome Estudante',
            'matricula': 'Matricula',
            'genero': 'Gênero',
            'data_nascimento1': '2022-05-25 00:00:00',
            'curso': 'Curso',
            'Identidade': 'Identidade',
            'renumeracao': 'Remuneração',
            'nome_Completo': 'Nome Completo',
            'cpf': 'CPF',
            'Data_Nascimento': '2022-05-25',
            'endereco': 'Endereço',
            'nrTelCelular': '1234567890',
            'status': 'Status'
        }
        quest = questSEconomico(**dados_validos)
        quest.full_clean()  # Verifica a validação dos dados

        def test_salvamento_dados(self):
        # Cria uma instância do modelo com dados válidos
            dados = {
            'modalidade': 'Modalidade',
            'nome_estudante': 'Nome Estudante',
            'matricula': 'Matricula',
            'genero': 'Gênero',
            'data_nascimento1':'2022-05-25 00:00:00',
            'curso': 'Curso',
            'Identidade': 'Identidade',
            'renumeracao': 'Remuneração',
            'nome_Completo': 'Nome Completo',
            'cpf': 'CPF',
            'Data_Nascimento': '2022-05-25',
            'endereco': 'Endereço',
            'nrTelCelular': '1234567890',
            'status': 'Status'
        }

            quest = questSEconomico(**dados)
            quest.save()  # Salva o objeto no banco de dados

        # Verifica se o objeto foi salvo corretamente
            self.assertEqual(questSEconomico.objects.count(), 1)
            self.assertEqual(questSEconomico.objects.first(), quest)



        def test_RenderHtml(self):
        # Dados válidos para preencher o formulário
            formulario =  questSEconomico(
            modalidade = 23.25 ,
            nome_estudante = 'Valor 2',
            matricula = 'Valor 2',
            genero =  'Valor 2',
            data_nascimento1 = '2022-05-25',
            curso = 'Valor 2',
            Identidade ='Valor 2',
            renumeracao =  'Valor 2',
            nome_Completo = 'Valor 2',
            cpf = 'Valor 2',
            Data_Nascimento = '2022-05-25',
            endereco =  'Valor 2',
            nrTelCelular =  'Valor 2',
            status = 'atleta'  
        )
            campos = formulario.full_clean()
            self.assertTrue(campos,msg='arquivo')
        
        
    
