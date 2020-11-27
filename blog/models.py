from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Making a custom manager sets to interact with the DB
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    # STATUS_CHOICES is the list, that is handed over to choices option of the field
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # slug is a short form for something containing only letters, numbers or hypens
    # A SlugField is used to store and generate URLs for dynamically generated web pages
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # User model is the defaut model for authentication in Django
    # CASCADE will delete the all the posts of a user if the related User is deleted
    # related_post attribute helps to access the related objects easily
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    # auto_now and auto_now_add are creation and modification T/S
    # auto_now_add is used for tracking when a new row in the DB was created as it saves the T/S when the row, was added to the DB
    # auto_now is used for tracking, when the row in the DB was last modified
    updated = models.DateTimeField(auto_now = True)
    # auto_now gives the current date time value
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # choices parameter helps to set the status field only to one of the given parameter


    class Meta:
        ordering = ('-publish',)
        # sorts the list of posts in the descending order when, we query the DB
        # Descinding order is specified, using the negative prefix

    def __str__(self):
        # Used to get the string representation of an object
        return self.title

    objects = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
