from rest_framework.authtoken.views import ObtainAuthToken

from educa.auth.users.serializers import UserAdminSerializer


# Create your views here.

class UserAdminView(ObtainAuthToken):
    serializer_class = UserAdminSerializer