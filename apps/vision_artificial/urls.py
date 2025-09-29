from django.urls import path
from .views import ReconocimientoFacialView, LogReconocimientoListView

urlpatterns = [
    path('vision/reconocer/', ReconocimientoFacialView.as_view(), name='reconocer-facial'),
    path('vision/logs/', LogReconocimientoListView.as_view(), name='logs-reconocimiento'),
]