from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('journey/', views.journey_view, name='journey'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path('guestbook/', views.guestbook_view, name='guestbook'),
]