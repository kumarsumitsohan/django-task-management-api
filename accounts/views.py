from rest_framework import generics, permissions

from .serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    Creates a new user account. Open to anyone (no auth required).
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeView(generics.RetrieveAPIView):
    """
    GET /api/auth/me/
    Returns the currently authenticated user's profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
