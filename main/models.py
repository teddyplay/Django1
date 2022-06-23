from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    diskription = models.TextField(verbose_name='Описание')
    director = models.ForeignKey(Director, on_delete=models.PROTECT,null=True)


    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'


    def __str__(self):
        return self.diskription



class Review(models.Model):
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT,null=True)



