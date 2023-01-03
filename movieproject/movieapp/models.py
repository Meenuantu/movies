from django.db import models

# Create your models here.
class movie(models.Model):
    movie_name=models.CharField(max_length=250)
    desc=models.TextField()
    movie_year=models.IntegerField()
    img=models.ImageField(upload_to='Images')

    def __str__(self):
        return self.movie_name