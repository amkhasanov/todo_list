from django.test import TestCase
from base import models

class TaskModel(TestCase):

    def setUp(self):
        self.task = models.Task.objects.create(title='Test Task')

    def testStr(self):
        self.assertEqual(
            str(self.task),
            'Test Task',
        )
