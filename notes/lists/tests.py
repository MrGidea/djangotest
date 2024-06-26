from contextlib import AbstractContextManager
from typing import Any
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item, list
# Create your tests here.

class HomePageTest(TestCase):
        
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
'''
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
'''

class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        List_user = list()
        List_user.save()

        first_item = Item()
        first_item.text = 'The first list item'
        first_item.list = List_user
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = List_user
        second_item.save()

        saved_list = list.objects.first()
        self.assertEqual(saved_list, List_user)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(first_saved_item.list, List_user)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, List_user)
        
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
    
class ListViewTest(TestCase):
    def test_passes_correct_list_to_template(self):
        other_list = list.objects.create()
        correct_list = list.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)

    def test_uses_list_template(self):

        List_user = list.objects.create()
        response = self.client.get(f'/lists/{List_user.id}/')
        #response = self.client.get('/lists/the-new-page/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = list.objects.create()
        Item.objects.create(text='itemey 1', list = correct_list)
        Item.objects.create(text='itemey 2', list = correct_list)
        other_list = list.objects.create()
        Item.objects.create(text='other list item 1', list = other_list)
        Item.objects.create(text='other list item 2', list = other_list)
        
        response = self.client.get(f'/lists/{correct_list.id}/')
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    
class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        other_list = list.objects.create()
        correct_list = list.objects.create()
        self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={'item_text': 'A new list item for an existing list'}
            )
        #response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_after_POST(self):
        #response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        #new_list = list.objects.first()
        other_list = list.objects.create()
        correct_list = list.objects.create()
        
        response = self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={'item_text': 'A new list item for an existing list'}
        )
        '''
        self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={'item_text': 'A new list item for an existing list'}
            )
        '''
        #response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/the-new-page/')
        #new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{correct_list.id}/')

        