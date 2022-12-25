from django.test import TestCase

# Create your tests here.


class TestSomething(TestCase):
    def test_dummy(self):
        self.assertEqual(5*10, 50)
    
    def test_dummy_2(self):
        self.assertIn(5, [1, 2, 3, 4, 5])