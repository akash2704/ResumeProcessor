from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import tempfile
import re
from pdfminer.high_level import extract_text
from .models import Candidate
from .serializers import CandidateSerializer

class ResumeExtractionView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('resume')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_file:
            temp_file.write(file.read())
            temp_file_path = temp_file.name

        try:
            text = extract_text(temp_file_path)
            
            # Updated regex patterns for more accuracy
            first_name = re.search(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b|\b[A-Z]+(?:\s[A-Z]+)*\b', text)
            email = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
            mobile_number = re.search(r'\+?\d{1,4}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}', text)

            candidate_data = {
                'first_name': first_name.group(0) if first_name else 'N/A',
                'email': email.group(0) if email else 'N/A',
                'mobile_number': mobile_number.group(0) if mobile_number else 'N/A'
            }

            serializer = CandidateSerializer(data=candidate_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)