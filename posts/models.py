from django.db import models

class Post(models.Model):
    user_id = models.IntegerField()
    
    # O ID do post que vem da API.
    # unique=True garante que não salvaremos o mesmo post duplicado.
    external_id = models.IntegerField(unique=True) 
    
    title = models.CharField(max_length=255)
    
    body = models.TextField()

    def __str__(self):
        return self.title
