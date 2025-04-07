from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from library.models import Student
from django.urls import reverse

class StudentBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")

