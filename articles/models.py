from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class Categories(models.Model):
    name=models.CharField('Ad',max_length=200,unique=True)
    slug=models.SlugField('Slug',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Bölmə"
        verbose_name_plural = "Bölmələr"
class Articles(models.Model):
    name=models.CharField('Ad',max_length=200,unique=True)
    cate=models.ForeignKey(to=Categories,verbose_name='Bölmə',on_delete=models.CASCADE,default=1)
    slug=models.SlugField('Slug',default='')
    img=models.URLField('Şəkil',default='https://cdn.dribbble.com/users/755603/screenshots/2592626/sad.gif')
    date=models.DateTimeField('Tarix',default=timezone.now)
    sale=models.BooleanField('Endirim',default=False)
    complated=models.BooleanField('Təhvil verildi',default=False)
    advertTrendTxt=models.TextField('Məqalə başlığı Trend üçün',default='Trend')
    desc=RichTextField('Məzmun',default='none')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Məqalə"
        verbose_name_plural = "Məqalələr"