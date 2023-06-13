from django.test import TestCase
from app.models import questSEconomico

class QuestSEconomicoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração dos dados de teste
        questSEconomico.objects.create(
            modalidade='Modalidade de Teste',
            nome_estudante= "Nome de Teste" ,
            matricula='Matrícula de Teste',
            genero='Gênero de Teste',
            data_nascimento1='2022-01-01',
            curso='Curso de Teste',
            Identidade='Identidade de Teste',
            renumeracao='Remuneração de Teste',
            nome_Completo='Nome Completo de Teste',
            cpf='CPF de Teste',
            Data_Nascimento='2022-01-01',
            endereco='Endereço de Teste',
            nrTelCelular= " ",
            status='Status de Teste'
        )

    def test_modalidade(self):
        quest = questSEconomico.objects.get(id=1)
        modalidade = quest.modalidade
        self.assertEqual(modalidade, 'Modalidade de Teste')

    def test_nome_estudante(self):
        quest = questSEconomico.objects.get(id=1)
        nome_estudante = quest.nome_estudante
        self.assertEqual(nome_estudante, 'Nome de Teste')

    def test_status(self):
        quest = questSEconomico.objects.get(id=1)
        status = quest.status
        self.assertEqual(status, 'Status de Teste')


    #cONTINUAÇAO DOS DEMAIS CAMPOS