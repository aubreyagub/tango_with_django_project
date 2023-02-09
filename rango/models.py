from django.db import models
from django.template.defaultfilters import slugify

# Create your models here

class Category(models.Model):
    max_length_cat=128 
    name = models.CharField(max_length=max_length_cat, unique=True)
    views = models.IntegerField(default=0) # stores integers
    likes = models.IntegerField(default=0) # stores integers
    slug = models.SlugField(unique=True)

    # turn urls like 'this%20is%20bad%20practice' to 'this-is-good-practice'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    max_length_page=128 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=max_length_page) # stores strings
    url = models.URLField() # stores resource URLs
    views = models.IntegerField(default=0) # stores integers

    def __str__(self):
        return self.title
