from django.urls import path
from . import views 

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('sources', views.sources, name='sources'),
    path('sources/<int:id>/', views.productdetail, name='productdetail'),
    path('sources/tur/<str:tur>', views.SpesificSource, name='SpesificSource'),


]