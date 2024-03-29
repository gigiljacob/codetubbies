from __future__ import unicode_literals

from collections import OrderedDict

from django.conf import settings
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import (PageNumberPagination, LimitOffsetPagination)


class RestPagination(PageNumberPagination, LimitOffsetPagination):
    """
    class FoobarPagiantion(RestPagination):
        page_size = 10


    class FoobarView(ListAPIView):
        pagination_class = FoobarPagiantion
    """

    def paginate_queryset(self, queryset, request, view=None):
        queryset = super().paginate_queryset(queryset, request, view=view)
        limit = request.query_params.get('limit')
        if str(limit).isdigit():
            return queryset[:int(limit)]
        return queryset

    def get_paginated_response(self, results):
        next_link = self.get_next_link() if self.get_next_link() is not None else ''
        prev_link = self.get_previous_link() if self.get_previous_link() is not None else ''

        if settings.USE_SSL:
            next_link = next_link.replace('http:', 'https:')
            prev_link = prev_link.replace('http:', 'https:')

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_size', self.page_size),
            ('current_page', self.page.number),
            ('next', next_link if next_link != '' else None),
            ('previous', prev_link if prev_link != '' else None),
            ('status', status.HTTP_200_OK),
            ('message', _('Success')),
            ('success', True),
            ('results', results)
        ]))