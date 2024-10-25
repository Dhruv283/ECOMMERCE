from django.test import TestCase

# Create your tests here.
class First_Test(TestCase):
    def setup(self):
        print("Hello")

    def test_eual(self):
        self.assertEqual(1,1)

