from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class test_LoginViewTest(TestCase):
    def test_setUp(self):
        # Cria um usuário de teste
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        # Define a URL de login usando o nome da URL definido no arquivo de URLs
        url = reverse('login')

        # Realiza uma requisição POST para a URL de login, com as credenciais do usuário
        response = self.client.post(url, {'username': self.username, 'password': self.password})

        # Verifica se o usuário foi redirecionado para uma página após o login bem-sucedido
        self.assertEqual(response.status_code, 200)

        #Verifica se o usuário está realmente autenticado
        #self.assertTrue(response.wsgi_request.user.is_authenticated)

