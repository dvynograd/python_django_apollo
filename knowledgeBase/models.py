from django.db import models
from django import forms
from datetime import datetime

class Tag (models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title    
    
    
    
class Jurisdiction (models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title        


class Memo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    jurisdictions = models.ManyToManyField(Jurisdiction)
    def __unicode__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    jurisdictions = models.ManyToManyField(Jurisdiction)
    def __unicode__(self):
        return self.title

    
class Faq(models.Model):        
    title = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    jurisdictions = models.ManyToManyField(Jurisdiction)
    def __unicode__(self):
        return self.title

    
class Library(models.Model):        
    title = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/documents/')
    tags = models.ManyToManyField(Tag)
    jurisdictions = models.ManyToManyField(Jurisdiction)
    def __unicode__(self):
        return self.title
    
    
class MemoComment(models.Model):    
    memo = models.ForeignKey(Memo)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.description



