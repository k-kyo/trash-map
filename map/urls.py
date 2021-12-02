from django.urls import path

from map.views import PointView, TspView

urlpatterns = [
    path('', PointView.as_view(), name='point'),
    path('tsp', TspView.as_view(), name='tsp'),
]
