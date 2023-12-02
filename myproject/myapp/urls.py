

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.login, name='login'),
# ]

# urls.py
# myapp/urls.py
# from django.urls import path

# # importing views from views..py
# from .views import LoginCreate
# urlpatterns = [
# 	path('', LoginCreate.as_view() ),
# ]
# myapp/urls.py
from django.urls import path
# from .views import create_view
from .import views

urlpatterns = [
    # path('create/', create_view, name='create_view'),
    # Add other URL patterns as 
    path('create/',views.create,name='create'),
    path('edit/',views.edit,name='edit'),
    path('list/',views.list,name='list'),

]


