from django.shortcuts import render

# Create your views here.
from rest_framework.reponse import Response
from rest_framework import status, views
from utils.validation_utils import is_valid_email

class EmailCheckView(views.APIView):

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "email is required"}, status=status.HTTP_400_BAD_REQUEST)

        if is_valid_email(email):
            return Response({"message": "valid email"}, status=status.HTTP_200_OK)
        else:
            return Response({"erroe":"Invalid email"}, status=status.HTTP_400_BAD_REQUESTS)