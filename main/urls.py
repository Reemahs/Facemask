from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/",views.index,name="index"),
    path("",views.home,name="home"),
    path("createRequest/",views.create,name="createRequest"),
    path('<int:request_id>/assign/', views.assign, name='assign'),
    path('<int:request_id>/unassign/', views.unassign, name='unassign'),
    path('<int:request_id>/complete/', views.complete, name='complete'),
    path('<int:request_id>/uncomplete/', views.uncomplete, name='uncomplete'),



]
