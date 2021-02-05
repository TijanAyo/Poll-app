from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('Poll_Question/<int:pk>/', views.detail.as_view(), name='detail'),
    path('<int:pk>/results/', views.result.as_view(), name='result'),
    path('<int:pk>/vote/', views.vote, name='vote')
]
