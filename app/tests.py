from django.test import TestCase


# Create your tests here.
class TestTest(TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_additional(self):
        self.assertTrue(True)