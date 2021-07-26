from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import tree
from datetime import datetime

def validate_file_extension(value):
  import os
  from django.core.exceptions import ValidationError
  ext = os.path.splitext(value.name)[1] # NOTE: selects suffix ex. png jpg
  valid_extensions = ['.jpg','.png']
  if ext.lower() not in valid_extensions:
    raise ValidationError('Unsupported  file extension.')


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) # NOTE:dont re-invent tire use default user things
  avatar = models.FileField(upload_to='files/user_cover',null=True,blank=True,validators=[validate_file_extension])
  description = models.CharField(max_length=512,null=False,blank=False)

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'

class Article(models.Model):
  title = models.CharField(max_length=128,null=False,blank=False)
  cover = models.FileField(upload_to='files/article_cover',validators=[validate_file_extension])
  content = RichTextField()
  created_at = models.DateTimeField(default=datetime.now,blank=False)
  category = models.ForeignKey('Category',on_delete=models.CASCADE)
  author = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

  def __str__(self):
    return self.title
class Category(models.Model):
  title = models.CharField(max_length=128,null=False,blank=False)
  cover = models.FileField(upload_to='files/category_cover',null=False,blank=False,validators=[validate_file_extension])
  
  def __str__(self):
    return self.title