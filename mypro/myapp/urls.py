from django.conf.urls import url
from . import views


app_name = 'myapp'

urlpatterns = [
    url(r'user_login/$',views.user_login,name='user_login'),
    url(r'^register/',views.register,name='register'),
]