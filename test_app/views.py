# from django.http import HttpResponse
# from test_app.models import Movie,MovieForm
#
# from django.shortcuts import render,redirect
#
# # Create your views here.
# def home(request):
#     movies=Movie.objects.all()
#     return render(request,'index.html',{'movies':movies})
# def getMovie(request,id):
#     movie=Movie.objects.get(id=id)
#     return render(request,'movie.html',{'movie': movie})
# def addMovie(request):
#     if request.method=='POST':
#         form=MovieForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('home')
#     return render(request,"addmovie.html",{'form':MovieForm()})
# def deleteMovie(request,id):
#     m=Movie.objects.get(id=id)
#     if request.method =='POST':
#         m.delete()
#         return redirect('home')
#     return render(request,"deletemovie.html", {'movie': m})
# def editMovie(request,id):
#     n=Movie.objects.get(id=id)
#     if request.method=='POST':
#         form=MovieForm(request.POST,instance=n)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('home')
#     return render(request,"editmovie.html",{'form':MovieForm(instance=n)})

from rest_framework import viewsets,serializers
from test_app.models import Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
