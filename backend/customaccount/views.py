from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def users_root(request, format=None):
    return Response({   
        'users list ':reverse("users",request=request,format=format),
        'user details': reverse('user-details', request=request, format=format),
    })


User = get_user_model()



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer