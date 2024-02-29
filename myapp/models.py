from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(null = False, unique = True, db_index = True, editable = False)

    def save(self, *args, **kwargs):    # SlugField for Categories
        self.slug = slugify(self.name)  
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}"

class MyApp(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="myapps")
    description = RichTextField()
    is_active = models.BooleanField(default = False)
    is_home = models.BooleanField(default = False)
    slug = models.SlugField(null = False,blank = True ,unique = True, db_index = True, editable = False)
    categories = models.ManyToManyField(Category)#, related_name='blog_set'
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):    # SlugField
        self.slug = slugify(self.title)  
        super().save(*args, **kwargs)


