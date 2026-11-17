from django.urls import path
from . import views
urlpatterns=[
    path('greeting/',views.greeting),
    path('student/',views.student),
    path('student2/',views.student2),
    path('go/',views.go),
    path('welcome_page/',views.welcome_view, name='welcome_page'),
    path('list/',views.show_list),
    path('list2/',views.show_list2),
    path('tuple1/',views.show_tuple),
]