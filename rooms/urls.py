from django.urls import path
from .views import home, create_room, update_room, room_delete, room, topics_page, activity

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('topics/', topics_page, name='topics'),
    path('activity/', activity, name='activity'),
    path('update-room/<int:id>/', update_room, name='update-room'),
    path('delete-room/<int:id>/', room_delete, name='delete-room'),
]