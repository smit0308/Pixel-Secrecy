from django.urls import path
from .views import home,encode_decode
urlpatterns = [
               path('',view=home,name='home'),
            #    path('encode',view=encode,name='encode'),
            #    path('decode',view=decode,name='decode'),
               path('encode_decode/', view=encode_decode, name='encode_decode'),
]
