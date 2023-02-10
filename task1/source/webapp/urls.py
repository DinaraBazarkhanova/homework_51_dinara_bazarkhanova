from django.urls import path

from source.webapp.views.cat_stats import add_view
from source.webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('cat_stats/', add_view)
]
