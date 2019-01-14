from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveAPIView,

)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from posts.models import Post
from posts.api.serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,

)


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostListApiView(ListAPIView):
    serializer_class = PostListSerializer
    search_filters = [SearchFilter, OrderingFilter]
    pagination_class = PostPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


# in this we assign the user to the post as author and also populate the post form while updating
class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDestroyApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'
