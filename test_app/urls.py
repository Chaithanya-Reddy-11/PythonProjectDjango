#
# from django.urls import path
# from test_app import views
#
# urlpatterns = [
#   path('home',views.home,name='home'),
#   path('movie/<int:id>',views.getMovie,name='getMovie'),
#   path('addMovie',views.addMovie,name='addMovie'),
#   path('deleteMovie/<int:id>',views.deleteMovie,name='deletemovie'),
#   path('editMovie/<int:id>',views.editMovie,name='editmovie'),
#
# ]

from rest_framework.routers import DefaultRouter
from test_app.views import MovieViewSet
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
urlpatterns = []
urlpatterns += router.urls
