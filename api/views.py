from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import BlogModel
from .serializers import BlogSerializers
from .permissions import IsOwner


# Create your views here.
class TenRequestMinThrottle(UserRateThrottle):
    rate = '10/min'


class ThreeRequestMinThrottle(AnonRateThrottle):
    rate = '3/min'


class HomeApiViews(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    throttle_classes = [TenRequestMinThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]

# class DetailBlog(RetrieveAPIView):

class DetailApiViews(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    throttle_classes = [TenRequestMinThrottle]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class UpdateApiViews(generics.RetrieveUpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'id'
    permission_classes = (IsOwner, IsAuthenticated)
    throttle_classes = [TenRequestMinThrottle]


class CreateApiViews(generics.CreateAPIView):
    serializer_class = BlogSerializers
    throttle_classes = [TenRequestMinThrottle]
    permission_classes = (IsOwner, IsAuthenticated)
    queryset = BlogModel.objects.all()


class DeleteApiViews(generics.DestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    throttle_classes = [TenRequestMinThrottle]
    permission_classes = (IsOwner, IsAuthenticated)
    lookup_field = "id"


class UserPostsApiViews(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    throttle_classes = [TenRequestMinThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return BlogModel.objects.filter(user=self.request.user)


class SortByField(generics.ListAPIView):
    queryset = BlogModel
    serializer_class = BlogSerializers
    throttle_classes = [TenRequestMinThrottle]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BlogModel.objects.all().order_by('title')
