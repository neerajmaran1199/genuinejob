from django.urls import path
from .views import home, PostCreateView, PostDetailView, contact, home2

urlpatterns = [
    path('', home, name='home-page'),
    path('postjob/', PostCreateView.as_view(), name='post-job'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('contact', contact, name='post-contact'),
    path('home2', home2, name='')

]