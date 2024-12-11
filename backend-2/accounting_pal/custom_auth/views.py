import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser  # Use CustomUser model
from rest_framework import status
from .serializers import CustomUserSerializer  # Updated serializer

class CreateUserView(APIView):
    """
    Handles the creation of a new user and sends a magic login link.
    """
    def post(self, request):
        # Extract data from the request
        email = request.data.get('email')
        first_name = request.data.get('first_name', '')  # Optional
        last_name = request.data.get('last_name', '')    # Optional
        role = request.data.get('role', 'other')  # Default to 'other'
        phone_number = request.data.get('phone_number', None)  # Optional
        
        # Check if email is provided
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the email already exists
        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'Email is already in use'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the new user
        user = CustomUser.objects.create(
            email=email,
            username=email,  # Use email as the username
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
            is_verified=False,  # Default to unverified
        )

        # Generate JWT token
        payload = {
            'user_id': user.id,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(minutes=15),  # Token expires in 15 minutes
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        # Create the magic link URL
        magic_link = f"{settings.EMAIL_VERIFICATION_URL}/magic-login?token={token}"

        # Attempt to send the magic link
        try:
            send_mail(
                subject='Your Magic Login Link',
                message=f"Click the link to log in: {magic_link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            return Response({'message': 'User created and magic link sent successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Handle email sending failure
            return Response({'error': f"User created, but failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDetailAndDeleteView(APIView):
    """
    Handles retrieving a user's details and deleting the user by primary key (pk).
    """
    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)  # Use CustomUser model
            serializer = CustomUserSerializer(user)  # Updated serializer
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)  # Use CustomUser model
            user.delete()
            return Response({'message': f'User with id {pk} has been deleted.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        

class RequestMagicLinkView(APIView):
    """
    Handles sending a magic login link to the user's email address.
    """

    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({'error': 'Email is required'}, status=400)

        # Attempt to find the user
        try:
            user = CustomUser.objects.get(email=email)  # Use CustomUser model
        except CustomUser.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=404)

        # Generate JWT token
        payload = {
            'user_id': user.id,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(minutes=15),  # Token expires in 15 minutes
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        # Create the magic link URL
        magic_link = f"{settings.EMAIL_VERIFICATION_URL}/magic-login?token={token}"

        # Attempt to send the magic link
        try:
            send_mail(
                subject='Your Magic Login Link',
                message=f"Click the link to log in: {magic_link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            return Response({'message': 'Magic link sent successfully'}, status=200)
        except Exception as e:
            return Response({'error': f"Failed to send email: {str(e)}"}, status=500)