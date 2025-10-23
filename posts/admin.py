from django.contrib import admin
from .models import Post

# Registra o modelo Post no admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'external_id')
    
    search_fields = ('title', 'body')

