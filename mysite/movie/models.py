from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    Movie_id = models.IntegerField(primary_key=True)
    Movie_Name = models.CharField(max_length=128,unique=True)
    Movie_Genre = models.CharField(max_length=128)
    Movie_Language = models.CharField(max_length=128,default='English')
    Movie_Plot = models.TextField()
    Movie_Year = models.IntegerField()
    Movie_Rating = models.FloatField(default=0)
    Movie_Imdb = models.URLField(default='')
    Movie_Poster = models.URLField(default='')
    Movie_Alt = models.CharField(max_length=50,default='')
    Movie_Trailer = models.URLField(default='')
    Movie_Price = models.IntegerField()

    def Publish(self):
        self.save()

    def __str__(self):
        return self.Movie_Name

class Rent(models.Model):
    Name = models.CharField(max_length=128,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE,default='')


class Seen(models.Model):
    user_name = models.CharField(max_length=128)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name + '|' + self.movie_id


class Watch(models.Model):
    user_name = models.CharField(max_length=128)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)


    def __str__(self):
        return self.user_name + '|' + self.movie_id


class Contact(models.Model):
    Name =models.CharField(max_length=128)
    From_Email = models.EmailField()
    Messages = models.TextField()
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
