# Django
from django.db import models
from django.utils.translation import ugettext as _

# Local
from flix.common.models import Tag

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('people')

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class ContentItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    us_release_date = models.DateField(verbose_name=_('US Release Date'))
    tags = models.ManyToManyField(Tag, related_name='%(class)s')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        unique_together = (
            ('name', 'us_release_date')
        )

class Movie(ContentItem):
    MPAA_RATINGS_CHOICES = (
        ('g', 'G'), 
        ('pg', 'PG'), 
        ('pg-13', 'PG-13'), 
        ('r', 'R'), 
        ('nc-17', 'NC-17'), 
        ('nr', 'NR')
    )

    mpaa_rating = models.CharField(verbose_name=_('MPAA Rating'), max_length=5, 
        choices=MPAA_RATINGS_CHOICES)
    director = models.ForeignKey(Person)

    def __str__(self):
        return self.name

class Series(ContentItem):
    US_TV_RATINGS_CHOICES = (
        ('tv-g', 'TV-G'), 
        ('tv-y', 'TV-Y'), 
        ('tv-y7', 'TV-Y7'), 
        ('tv-pg', 'TV-PG'), 
        ('tv-14', 'TV-14'), 
        ('tv-ma', 'TV-MA')
    )

    us_tv_parental_rating = models.CharField(verbose_name=_('Parental Rating'), 
        max_length=5, choices=US_TV_RATINGS_CHOICES)

    class Meta:
        verbose_name_plural = 'series'

    def __str__(self):
        return self.name

class Episode(models.Model):
    series = models.ForeignKey(Series)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    season = models.PositiveSmallIntegerField(default=1)
    director = models.ForeignKey(Person)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('series', 'title')
        )

    def __str__(self):
        return '{0} - {1}'.format(self.series.name, self.title)
