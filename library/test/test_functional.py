from django.urls import reverse
from rest_framework.test import APITestCase
from library.models import Student
from library.test.TestUtils import TestUtils

class StudentFunctionalTest(APITestCase):

    def test_create_student(self):
        """Test if a student is created successfully"""
        test_obj = TestUtils()
        try:
            student = Student.objects.create(name="Alice", roll_number=1)
            if student:
                test_obj.yakshaAssert("TestCreateStudent", True, "functional")
                print("TestCreateStudent = Passed")
            else:
                test_obj.yakshaAssert("TestCreateStudent", False, "functional")
                print("TestCreateStudent = Failed")
        except:
            test_obj.yakshaAssert("TestCreateStudent", False, "functional")
            print("TestCreateStudent = Failed")

    def test_student_list_view(self):
        """Test if the student list page loads successfully"""
        test_obj = TestUtils()
        try:
            Student.objects.create(name="Alice", roll_number=1)
            Student.objects.create(name="Bob", roll_number=2)

            response = self.client.get(reverse("student-list"))
            if response.status_code == 200 and "Alice" in response.content.decode():
                test_obj.yakshaAssert("TestStudentListView", True, "functional")
                print("TestStudentListView = Passed")
            else:
                test_obj.yakshaAssert("TestStudentListView", False, "functional")
                print("TestStudentListView = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestStudentListView", False, "functional")
            print("TestStudentListView = Failed")
