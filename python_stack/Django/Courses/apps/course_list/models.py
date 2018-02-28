# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'The course name should be more than 5 characters'
        if len(postData['description']) < 15:
            errors['desc'] = 'The course description must be longer than 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
