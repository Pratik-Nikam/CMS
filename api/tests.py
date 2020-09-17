from django.test import TestCase
from api.models import Content
"""

class Content(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Content.objects.create(title='test blog', body="alnla", summary='This is summary', categories='Black')
        Content.objects.create(
            title='Muffin', body=1, summary='Gradane', categories='Brown')

    def test_content(self):
        content_get = Content.objects.get(name='test blog')
        content_get1 = Content.objects.get(name='Muffin')
        self.assertEqual(
            content_get.get_breed(), "Belong to Black.")
        self.assertEqual(
            content_get1.get_breed(), "belong to Brown.")
            
"""