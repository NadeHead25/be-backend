from operator import truediv
from django.db import models

# Create your models here.
class Notice(models.Model):
    notice_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.notice_text    
