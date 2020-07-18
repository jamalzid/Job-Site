from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
Job_Type=[

    ('part time', 'part time'),
    ('full time', 'full time')
]


class Job(models.Model):
    owner=models.ForeignKey(User ,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='media/images/')
    city = models.CharField(max_length=200)
    contry=models.CharField(max_length=200)
    job_type = models.CharField(max_length=10, choices=Job_Type)
    published_at=models.DateTimeField(auto_now_add=True)
    salary=models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    def __str__(self):
        return self.title


class Comment(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.EmailField()
    comment=models.TextField()
    published_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name




class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='media/cv/')
    letter = models.TextField()
    apply_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
