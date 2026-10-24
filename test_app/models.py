from django.db import models
from django.forms.models import ModelForm

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField()
    review=models.FloatField()
    director=models.CharField(max_length=100)
    writer=models.CharField(max_length=100)
    producer=models.CharField(max_length=100)
    genre=models.CharField(max_length=100,null=True)
    music_director=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title}-{self.director}"

class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields='__all__'