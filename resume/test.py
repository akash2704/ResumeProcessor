import os
from django.test import TestCase, Client
from rest_framework import status

class ResumeExtractionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.resume_file_path = r"D:\akash programs\Xinterview entrance\ResumeProcessor\Untitled-resume.pdf"


    def test_upload_resume_and_extract_details(self):
        with open(self.resume_file_path, 'rb') as resume_file:
            response = self.client.post('/api/extract_resume/', {'resume': resume_file})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('first_name', response.data)
        self.assertIn('email', response.data)
        self.assertIn('mobile_number', response.data)

    def test_upload_without_resume_file(self):
        response = self.client.post('/api/extract_resume/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)