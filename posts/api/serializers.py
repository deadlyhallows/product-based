from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from posts.models import Post

post_detail_url = HyperlinkedIdentityField(
         view_name='posts-api:detail',
         lookup_field = 'slug')

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'user',
            'url',
            'title',
            'content',
            'publish',

        )
    def get_user(self, obj):
        return str(obj.user.username)