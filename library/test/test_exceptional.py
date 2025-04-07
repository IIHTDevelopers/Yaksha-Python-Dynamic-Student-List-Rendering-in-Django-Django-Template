
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from library.models import Student
class StudentExceptionalTest(APITestCase):


    def test_duplicate_roll_number(self):
        test_obj = TestUtils()
        try:
            Student.objects.create(name="Alice", roll_number=1)
            Student.objects.create(name="Bob", roll_number=1)  # Duplicate roll number

            test_obj.yakshaAssert("TestDuplicateRollNumber", False, "exceptional")
            print("TestDuplicateRollNumber = Failed")
        except IntegrityError as e:
            if "roll_number" in str(e):  # Checking if the error is specifically for duplicate roll number
                test_obj.yakshaAssert("TestDuplicateRollNumber", True, "exceptional")
                print("TestDuplicateRollNumber = Passed")
            else:
                test_obj.yakshaAssert("TestDuplicateRollNumber", False, "exceptional")
                print("TestDuplicateRollNumber = Failed with unexpected error")
        except Exception as e:
            test_obj.yakshaAssert("TestDuplicateRollNumber", False, "exceptional")
            print("TestDuplicateRollNumber = Failed")

    def test_empty_student_list(self):
        """Test if the page handles no students gracefully"""
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse("student-list"))
            if response.status_code == 200 and "No students found" in response.content.decode():
                test_obj.yakshaAssert("TestEmptyStudentList", True, "exceptional")
                print("TestEmptyStudentList = Passed")
            else:
                test_obj.yakshaAssert("TestEmptyStudentList", False, "exceptional")
                print("TestEmptyStudentList = Failed")
        except:
            test_obj.yakshaAssert("TestEmptyStudentList", False, "exceptional")
            print("TestEmptyStudentList = Failed")
