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

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'user',
            'url',
            'title',
            'slug',
            'content',
            'publish',
            'image',
            'html'
        )
    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_html(self, obj):
        return obj.get_markdown()