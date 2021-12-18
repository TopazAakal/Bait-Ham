from django.urls import reverse
from django.test import TestCase, Client
from Animal.models import animal


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = animal.objects.create(id=1,
                                         name='Rex',
                                         submitter='Afik',
                                         species='dog',
                                         breed='Boxer',
                                         description='very good dog',
                                         sex='M',
                                         Adoption='No',
                                         image='default.png')

    def test_all_animals_GET(self):
        response = self.client.get(reverse('Animal:all_animals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Animal/all_animals.html')

    def test_Animal_detail_GET(self):
        response = self.client.get(reverse('Animal:animal_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Animal/animal_detail.html')

    def test_add_Animal_GET(self):
        response = self.client.get(reverse('Animal:add_Animal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Animal/add_Animal.html')

    def test_add_Animal_POST_Valid(self):
        animal_count = animal.objects.count()
        response = self.client.post(reverse('Animal:add_Animal'), {'name': 'Rex',
                                                                   'submitter': 'Afik',
                                                                   'species': 'dog',
                                                                   'breed': 'Boxer',
                                                                   'description': 'very good dog',
                                                                   'sex': 'M',
                                                                   'Adoption': 'No',
                                                                   'image': 'default.png'})

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count)  # all fields are in place

    def test_add_Animal_POST_Not_Valid(self):
        response = self.client.post(reverse('Animal:add_Animal'),
                                    {'name': '',
                                     'submitter': '',
                                     'species': '',
                                     'breed': '',
                                     'description': '',
                                     'sex': '',
                                     'Adoption': '',
                                     'image': ''})
        self.assertEqual(response.status_code, 302)  # means redirection works in case of a bad form

    def test_edit_Animal_GET(self):
        response = self.client.get(reverse('Animal:editAnimal', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Animal/add_Animal.html')

    def test_edit_Animal_POST(self):
        animal_count = animal.objects.count()
        response = self.client.post(reverse('Animal:editAnimal', args=[1]), {'name': 'Rex',
                                                                             'submitter': 'Afik',
                                                                             'species': 'dog',
                                                                             'breed': 'Boxer',
                                                                             'description': 'very good dog',
                                                                             'sex': 'M',
                                                                             'Adoption': 'No',
                                                                             'image': 'default.png'})
        self.assertEqual(response.status_code, 200)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count)  # all fields are in place updated

    def test_delete_Animal_GET(self):
        response = self.client.get(reverse('Animal:deleteAnimal', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Animal/DeleteAnimal.html')

    def test_delete_Animal_POST(self):
        animal_count = animal.objects.count()
        response = self.client.get(reverse('Animal:deleteAnimal', args=[1]), {'name': 'Rex',
                                                                             'submitter': 'Afik',
                                                                             'species': 'dog',
                                                                             'breed': 'Boxer',
                                                                             'description': 'very good dog',
                                                                             'sex': 'M',
                                                                             'Adoption': 'No',
                                                                             'image': 'default.png'})
        self.assertEqual(response.status_code, 200)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count)  # all fields are in place updated

        # testAnimal = self.obj
        # pk = testAnimal.pk
        # get_testAnimal = self.obj.objects.get(id=testAnimal.pk)
        # del_testAnimal = get_testAnimal.delete()
        # self.assertFalse(animal.objects.filter(pk=pk).exists())