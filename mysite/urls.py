from django.urls import path
from .views import home, actor, contact


urlpatterns = [
    # path('', home,name='home'),
    # path('data/', actor, name="actor"),
    path('', contact, name='contact')
]