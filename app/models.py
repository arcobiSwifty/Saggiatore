from django.db import models

class ReleaseYear(models.Model):
    year = models.IntegerField(default=2018)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "anno"
        verbose_name_plural = "anni"


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "argomento"
        verbose_name_plural = "argomenti"


class Article(models.Model):

    release_year = models.ForeignKey(ReleaseYear, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=7000)
    author = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True, blank=True)
    argument = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "articolo"
        verbose_name_plural = "articoli"


class Edition(models.Model):
    release_year = models.ForeignKey(ReleaseYear, on_delete=models.CASCADE)
    #articles = models.ManyToMany(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.release_year.year)

    class Meta:
        verbose_name = "edizione"
        verbose_name_plural = "edizioni"