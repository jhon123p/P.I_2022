from django.test import TestCase
from django.urls import reverse




class test_views(TestCase):

    def test_views_home(self):
        url = reverse('home')

        response = self.client.get(url)

        self.assertTemplateUsed(response , 'home.html')
        
        self.assertEquals(response.status_code , 200)

        #self.assertRedirects(response , reverse('inscricoes'), status_code = 200 ,  target_status_code = 302)


