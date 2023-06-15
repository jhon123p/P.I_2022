from django.test import TestCase
from django.urls import reverse




class test_views(TestCase):

    def test_views_home(self):
        url = reverse('index')

        response = self.client.get(url)

        self.assertTemplateUsed(response , 'registration/login.html')

        #self.assertRedirects(response , reverse('inscricoes'), status_code= 200 , target_status_code = 302)

        #self.assertContains(response, "ththrh  htrhtrhtr h")

    def test_Funcional(self):
        response = self.client.get(reverse('inscricoes'))

        self.assertEqual(response.status_code , 302)