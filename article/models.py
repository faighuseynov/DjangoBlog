from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete='models.CASCADE', verbose_name='Yazıçı')
    title = models.CharField(max_length=50, verbose_name='Başlıq')
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Qeyd edilmə tarixi')
    article_image = models.FileField(blank=True, null=True, verbose_name='Məqaləyə şəkil əlavə edin')
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']



