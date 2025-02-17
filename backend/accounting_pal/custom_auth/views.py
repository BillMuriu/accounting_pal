import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User


class RequestMagicLinkView(APIView):
    """
    Handles sending a magic login link to the user's email address.
    """
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({'error': 'Email is required'}, status=400)

        # Attempt to find or create the user
        user, created = User.objects.get_or_create(email=email)

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


class VerifyMagicLinkView(APIView):
    """
    Handles token verification and logs the user in if the token is valid.
    """
    def post(self, request):
        token = request.data.get('token')
        
        if not token:
            return Response({'error': 'Token is required'}, status=400)

        try:
            # Decode the JWT token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token has expired'}, status=400)
        except jwt.InvalidTokenError:
            return Response({'error': 'Invalid token'}, status=400)

        user_id = payload.get('user_id')
        
        if not user_id:
            return Response({'error': 'Invalid payload in token'}, status=400)

        try:
            # Fetch user
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        # Log in the user using Django's login system
        login(request, user)

        return Response({'message': 'Login successful'}, status=200)
