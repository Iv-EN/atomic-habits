from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    page_size_query_param = "page_size"

    def __init__(self):
        self.page_size = getattr(settings, "PAGINATOR_HABITS_PAGE_SIZE")
        self.max_page_size = getattr(
            settings, "PAGINATOR_HABITS_MAX_PAGE_SIZE"
        )
