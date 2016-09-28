from __future__ import unicode_literals

from django.db import models

class service(models.Model):
      title = models.CharField(max_length=200)
      body = models.TextField()
      created_date=models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.title
      
