from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)

#limits number of objects to be displayed
class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

#decides the number of pages in which pagination should be done
class PostPageNumberPagination(PageNumberPagination):
    page_size = 2